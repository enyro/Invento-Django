from django.shortcuts import render,redirect
from users.models import role, user_role
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .forms import RegisterForm
from django.contrib.auth import authenticate, login, logout

# Create your views here.
def create(request):
    if request.method == 'GET':
        roles = role.objects.order_by('id').all()
        form  = RegisterForm() 
        return render(request, 'create-user.html', {'form': form, 'roles':roles})
    if request.method == 'POST':
        form  = RegisterForm(request.POST)
       
        if form.is_valid():
            role_id = request.POST['role']
            role_data = role.objects.get(id=role_id)
            form.save()
            username = form.cleaned_data.get('username')
            user_data = User.objects.get(username=username)
            add_user_role = user_role(
                user = user_data,
                role = role_data
            )
            add_user_role.save()
            messages.success(request, 'Account was created for ' + username)
            return redirect('users')
        else:
            print('Form is not valid')
            messages.error(request, 'Error Processing Your Request')
            roles = role.objects.order_by('id').all() 
            return render(request, 'create-user.html', {'form': form, 'roles':roles})
    return render(request, 'create-user.html', {})
def signin(request):
    logout(request)
    if request.method == "GET": 
        return render(request,'signin.html',{})
    if request.method == "POST": 
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return redirect('home')
         
    return render(request,'signin.html',{})

def signout(request):
    logout(request) 
    return redirect('signin')

def users(request):
    users = User.objects.order_by('id').all()
    return render(request,'users.html',{'nbar':'users','users':users})
