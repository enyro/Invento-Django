from django.shortcuts import render,redirect
from users.models import Role, UserRole 
from django.contrib.auth.models import User 
from .forms import RegisterForm
from django.contrib.auth import authenticate, login, logout
from django.http import JsonResponse

def signin(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        return render(request, 'signin.html', {}) 

def signout(request):
    logout(request)
    return redirect('signin')

def signinApi(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(username=username, password=password)
    if user is not None:
        if user.is_active:
            login(request, user)
            return JsonResponse({'id': 200, 'data':"Signed in successfully!"})

        return JsonResponse({'id': 400, 'data': "Entered user is not active!"})

    return JsonResponse({'id': 400, 'data': "Invalid username or password!"})

def users(request): 
    if request.user.is_authenticated and request.user.userrole.role.role == 'Admin':
        roles = Role.objects.order_by('id').all()
        form = RegisterForm()
        return render(request, 'users.html', {'nbar': 'users', 'form': form, 'roles': roles})
    else:
        return redirect('home')

def getUsers(request):
    if request.user.is_authenticated and request.user.userrole.role.role == 'Admin':
        roleId = request.GET['role']
        if roleId != '0':
            roleFilter = Role.objects.get(id=roleId)
            users = User.objects.order_by('id').all().values('id', 'username','email','first_name','last_name','userrole__role__role').filter(userrole__role=roleFilter)
        else:
            users = User.objects.order_by('id').all().values('id', 'username','email','first_name','last_name','userrole__role__role')

        return JsonResponse({'id': 200, 'data': list(users)})

def create(request): 
    if request.user.is_authenticated and request.user.userrole.role.role == 'Admin':
        username = request.POST['username']
        fname = request.POST['fname']
        lname = request.POST['lname']
        roleId = request.POST['role']
        email = request.POST['email']
        password = request.POST['password'] 

        usernameExist = User.objects.filter(username=username).count()
        if usernameExist == 0 :
            create_user = User(
                email=email,
                first_name=fname,
                last_name=lname,
                username=username,
                password=password 
            )
            create_user.save()

            if create_user.id is not None:
                role_data = Role.objects.get(id=roleId)
                add_user_role = UserRole(
                    user=create_user,
                    role = role_data
                )
                add_user_role.save()
                return JsonResponse({'id': 200, 'data': "User created successfully!!"})
            else:
                return JsonResponse({'id': 400, 'data': "Failed to create!!"})
        else:
            return JsonResponse({'id': 400, 'data': "Username already exists!!"})
