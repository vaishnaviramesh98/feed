from django.shortcuts import render,redirect
from .models import CustomUser
from django.contrib import messages

# Create your views here.


def register(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        dob = request.POST['dob']
        username = request.POST['username']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        email = request.POST['email']

        if password1==password2:
            if CustomUser.objects.filter(username=username).exists():
                messages.info(request,'Username Taken')
                return redirect('register')
            elif CustomUser.objects.filter(email=email).exists():
                messages.info(request,'Email Taken')
                return redirect('register')
            else:   
               user = CustomUser.objects.create_user(username=username,dob=dob, password=password1, email=email,first_name=first_name,last_name=last_name)
               user.save();
               print('user created')
               
                

        else:
            messages.info(request,'password not matching..')    
            return redirect('register')
        return redirect('/')
    else:
        return render(request,'register.html')


def home(request):
    return render(request,'home.html')