from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User, auth
from django.contrib import messages

from .forms import SignupForm


def signup(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = SignupForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required

            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            username = form.cleaned_data['username']
            password1 = form.cleaned_data['password1']
            password2 = form.cleaned_data['password2']
            email = form.cleaned_data['email']


            if password1 == password2:
                if User.objects.filter(email=email).exists():
                    messages.info(request, 'Email already taken')
                elif User.objects.filter(username=username).exists():
                    messages.info(request, 'Username already taken')
                else:
                    user = User.objects.create_user(username=username, password=password1, email=email, first_name=first_name, last_name=last_name)
                    user.save()
                    messages.info(request, 'Registered')
            else:
                messages.info(request, 'Password not matching')
            
            # redirect to a new URL:
            return redirect('/accounts/register')

        # if the form is not valid
        else:
            messages.info(request, 'form is not valid')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = SignupForm()

    return render(request, 'signup/index.html', {'form': form})

