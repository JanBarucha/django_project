from django.urls import path
from . import views


urlpatterns = [
    path('generate_password', views.generate_password, name='generate_pass')
]