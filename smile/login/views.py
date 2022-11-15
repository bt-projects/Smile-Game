from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from .models import DemoSmile
from django.contrib.auth.models import User, auth
from django.contrib import messages

def index(request):
    # template = loader.get_template('')
    smile = DemoSmile.objects.all()
    context = {
        'smile': smile
    }

    if request.method == 'POST':
        # email = request.POST['email']
        username = request.POST['username']
        password = request.POST['password']

        # user = auth.authenticate(email=email, password=password)
        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            messages.info(request, 'sucessfull login')
            return redirect("/")
        else:
            messages.info(request, 'invalid credentails')
            return redirect("/")
    else:
        # return render(request, 'login/index.html')
        return render(request, 'login/index.html')

    # return render(request, 'login/index.html', context)