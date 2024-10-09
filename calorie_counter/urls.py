"""
URL configuration for calorie_counter project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from calorie_tracker import views




urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index, name="index"),
    path('foodentry/',views.foodEntry, name = "foodentry"),
    path('foodlist/',views.foodlist, name = "foodlist"),
    path('login_user/',views.login_user, name= "login_user.html"),
    path('register/',views.register, name="register.html"),
    path('logout_user',views.logout_user, name="logout_user"),
    path('foods/<int:food_id>/remove/',views.delete_food, name="delete_food"),
    path('foods/<int:food_id>/reset/',views.reset_calories, name="reset_calories"),
]
