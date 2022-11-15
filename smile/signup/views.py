from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User, auth
from django.contrib import messages

# Create your views here.
def signup(request):

    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        email = request.POST['email']

        if password1 == password2:
            if User.objects.filter(email=email).exists():
                messages.info(request, 'EMail already taken')
            elif User.objects.filter(username=username).exists():
                messages.info(request, 'Username already taken')
            else:
                user = User.objects.create_user(username=username, password=password1, email=email, first_name=first_name, last_name=last_name)
                user.save()
                messages.info(request, 'Registered')
        else: 
            messages.info(request, 'Password not matching')
            return redirect('signup/index.html')
        
        return redirect('/')
    
    else:
        return render(request, 'signup/index.html')
