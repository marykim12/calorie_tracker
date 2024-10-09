
from django.contrib import admin
from django.urls import path
from calorie_tracker import views

urlpatterns = [
    path('', views.index, name='index'), 
    path('login/', views.login_user, name='login_user'),  
    path('logout/', views.logout_user, name='logout_user'),  
    path('register/', views.register, name='register'),  
]