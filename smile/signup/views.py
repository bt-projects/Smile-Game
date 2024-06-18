from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User, auth
from django.contrib import messages

from .forms import SignupForm

#################################################################################
from django.contrib.auth import login, logout, authenticate, get_user_model
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_str
from django.core.mail import EmailMessage, BadHeaderError
from django.template.loader import render_to_string
from django.contrib.sites.shortcuts import get_current_site
from .tokens import account_activation_token

def activate(request, uidb64, token):
    User = get_user_model()
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except:
        user = None

    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()

        messages.success(request, "Thank you for your email confirmation. Now you can login your account.")
        return redirect('/accounts/login/')
    else:
        messages.error(request, "Activation link is invalid!")

    return redirect('/')

def activateEmail(request, user, to_email):
    mail_subject = "Activate your user account."
    message = render_to_string("signup/template_activate_account.html", {
        'user': user.username,
        'domain': get_current_site(request).domain,
        'uid': urlsafe_base64_encode(force_bytes(user.pk)),
        'token': account_activation_token.make_token(user),
        "protocol": 'https' if request.is_secure() else 'http'
    })

    email = EmailMessage(mail_subject, message, to=[to_email])
    
    try:
        if email.send():
            messages.success(request, f'Dear {user}, Registered, please go to you email {to_email} inbox and click on \
                    received activation link to confirm and complete the registration. Note: Check your spam folder.')
        else:
            messages.error(request, f'Problem sending email to {to_email}, check if you typed it correctly.')
    except BadHeaderError:
        messages.error(request, 'Invalid header found.')
    except Exception as e:
        messages.error(request, f'An error occurred: {e}')
        # logger.error(f'Error sending activation email: {e}')

#################################################################################

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
                    
                    ################################ added
                    # user1 = form.save(commit=False)
                    user.is_active=False
                    ################################

                    user.save()

                    ################################
                    activateEmail(request, user, form.cleaned_data.get('email'))
                    ################################

                    # messages.success(request, 'Registered')
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

