from django.urls import path
from . import views

app_name = "resetpassword"

urlpatterns = [
    path('', views.resetpassword, name="resetpassword")
]