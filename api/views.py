from django.shortcuts import render,redirect
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from rest_framework.decorators import api_view
# Create your views here.

def home(request):
    return render(request,'home.html',context={"page":"home"})

def register_page(request):

    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = User.objects.filter(username=username)
        if user.exists():
            messages.error(request,'Username already exists !!')
            return redirect('/register/')

        user = User.objects.create(
            first_name=first_name,
            last_name=last_name,
            username=username,
        )
        user.set_password(password)
        user.save()

        messages.success(request,'Successfully registered !!')

        return redirect('/login/')

    return render(request,'register.html',context={'page':'Register'})

def login_page(request):

    if request.method == 'POST':

        username = request.POST.get('username')
        password = request.POST.get('password')

        if not User.objects.filter(username=username).exists() or authenticate(username=username,password=password) is None:
            messages.error(request,'Wrong username or Password')
            return redirect('/login/') 
        else:
            user = authenticate(username=username,password=password)
            login(request,user)
            return redirect('/tasks/')
 
    return render(request,'login.html',context={'page':'Login'})

def logout_page(request):
    logout(request,)
    return redirect('/login/')

@login_required(login_url='/login/')
def tasks(request):

    if request.method == "POST":
        data = request.POST
        title = data.get('title')
        description = data.get('description')
        date = data.get('date')
        print(title)
        print(date)
        print(request.user)

        task = Tasks.objects.create(
            user = User.objects.filter(username=request.user)[0],
            title = title,
            description = description,
            date = date
        )
        task.save()
        return redirect('/tasks/')

    queryset ={}

    if request.GET.get('search'):
        queryset = Tasks.objects.filter(title__icontains = request.GET.get('search'))
    else:
        queryset = Tasks.objects.filter(user = User.objects.get(username =request.user))

    return render(request,'tasks.html',context={'page':'Tasks','tasks':queryset})

@api_view(["GET","PUT","POST"])
@login_required(login_url='/login/')
def update_task(request,id):
    print(id)
    queryset = Tasks.objects.get(id=id)
    print(request.method)

    if request.method =='PUT' or request.method == 'POST':
        
        # print(request.body.decode('utf-8'))
        data = request.data
        # data = json.loads(request.body.decode)
        title = data.get('title')
        description = data.get('description')
        date = data.get('date')

        queryset.title = title
        queryset.description = description

        if date:
            queryset.date = date

        queryset.save()

        return redirect('/tasks/')

    return render(request,'update_task.html',context={'page':'Update Task','task':queryset})

@login_required(login_url='/login/')
def delete_task(request,id):
    print(id)
    queryset = Tasks.objects.get(id = id)
    queryset.delete()    
    return redirect('/tasks/')