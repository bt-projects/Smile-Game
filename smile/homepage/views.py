from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    context = {
        
    }
    # return HttpResponse("This is home page")
    return render(request, 'homepage/index.html')
