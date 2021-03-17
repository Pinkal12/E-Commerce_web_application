from django.shortcuts import render , redirect
from django.http import HttpResponse
from django.contrib.auth.models import User, auth
from django.contrib import messages


# Create your views here.



def home(request):
    return render(request,'pages/index.html')

def about(request):
    return render(request,'pages/about.html')

def store(request):
    return render(request,'pages/store.html')

def cart(request):
    return render(request,'pages/cart.html')

def login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            messages.success(request,'You are now logged in')
            return redirect('home')
        else:
            messages.error(request,'invalid credantials')
            return redirect('login')    
    else:
        return render(request,'pages/login.html')

def signup(request):
    if request.method == "POST":

        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        if password1 == password2:
            if User.objects.filter(username=username).exists():
               messages.error(request,'Username already taken!')
            
            elif User.objects.filter(email=email).exists():
                 messages.error(request,'Email already taken!')
            else:
                 user = User.objects.create_user(first_name=first_name,last_name=last_name,username=username,email=email,password=password1)
                 user.save()
                 messages.success(request,"You are successfully registered!")
                 return redirect('login')
    else:
        return render(request,'pages/signup.html')

def logout(request):
    auth.logout(request)
    messages.success(request,'You have been logout!')
    return redirect("home")        

