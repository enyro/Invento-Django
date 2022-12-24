from django.shortcuts import render,redirect
from users.models import Role, UserRole 
from django.contrib.auth.models import User  
from django.contrib.auth import authenticate, login, logout
from django.http import JsonResponse
from django.core.mail import send_mail

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
            # send_mail(
            #     'Subject here',
            #     'Here is the message.',
            #     'from@example.com',
            #     ['to@example.com'],
            #     fail_silently=False,
            # )
            login(request, user)
            return JsonResponse({'id': 200, 'data':"Signed in successfully!"})

        return JsonResponse({'id': 400, 'data': "Entered user is not active!"})

    return JsonResponse({'id': 400, 'data': "Invalid username or password!"})

def users(request): 
    if request.user.is_authenticated and request.user.userrole.role.role == 'Admin':
        roles = Role.objects.order_by('id').all() 
        return render(request, 'users.html', {'nbar': 'users', 'roles': roles})
    else:
        return redirect('home')

def getUsers(request):
    if request.user.is_authenticated and request.user.userrole.role.role == 'Admin':
        roleId = request.GET['role']
        if roleId != '0':
            roleFilter = Role.objects.get(id=roleId)
            users = User.objects.order_by('id').all().values('id', 'username','email','first_name','last_name','userrole__role__role').filter(userrole__role=roleFilter)
        else:
            users = User.objects.order_by('id').all().values('id', 'username','email','first_name','last_name','userrole__role__role','userrole__role__id')

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
            create_user.set_password(password)
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

def resetPassword(request):
    return render(request,'reset-password.html',{})

def resetPasswordApi(request):
    currentPassword = request.POST['current']
    newPassword = request.POST['new']
    username = request.user.username
    if request.user.check_password(currentPassword):
        request.user.set_password(newPassword)
        request.user.save()
        user = authenticate(username=username, password=newPassword)
        login(request, user)
        return JsonResponse({'id': 200, 'data': "Password updated successfully!!"})
    else:
        return JsonResponse({'id': 400, 'data': "Incorrect current password!!"})

def editUser(request):
    id = request.POST['id']
    email = request.POST['email']
    fname = request.POST['fname']
    lname = request.POST['lname']
    roleId = request.POST['role']

    user = User.objects.get(pk=id)
    user.email = email
    user.first_name = fname
    user.last_name = lname
    user.email = email
    
    role = Role.objects.get(pk=roleId)
    user_role = UserRole.objects.get(user=user)
    user_role.role = role

    user.save()
    user_role.save()

    return JsonResponse({'id':200,'data':"User updated successfully!!"})

def resetPasswordAdminApi(request):
    id = request.POST['id']
    password = request.POST['password']
    user = User.objects.get(pk=id)
    user.set_password(password)
    user.save()

    return JsonResponse({'id':200,'data':"Password updated successfully!!"})