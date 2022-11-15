from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    context = {
        
    }
    # return HttpResponse("This is home page")
    return render(request, 'homepage/index.html')
