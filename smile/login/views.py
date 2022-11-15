from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import DemoSmile

def index(request):
    # template = loader.get_template('')
    smile = DemoSmile.objects.all()
    context = {
        'smile': smile
    }

    return render(request, 'login/index.html', context)