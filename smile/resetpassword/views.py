from django.shortcuts import render

# Create your views here.

def resetpassword(request):
    return render(request, 'resetpassword/index.html')

