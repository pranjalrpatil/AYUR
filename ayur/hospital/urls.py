from django.urls import path
from . import views

app_name = "hospital"

urlpatterns = [
    path('', views.HomePage, name='home'),
]