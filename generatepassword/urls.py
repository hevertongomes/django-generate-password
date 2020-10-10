from django.urls import path
from generate import views


urlpatterns = [
    path('', views.home, name='home'),
    path('password', views.password, name='password'),
]
