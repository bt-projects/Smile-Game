from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages


def login(request):
    # if user is already logged in redirect to the homepage
    if request.user.is_authenticated:
        return redirect("/")

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect("/")
        else:
            messages.info(request, 'invalid credentails')
            return render(request, 'registration/login.html')
    else:
        return render(request, 'registration/login.html')

def logout(request):
    auth.logout(request)
    return redirect('/')
