from django.shortcuts import render,redirect,get_object_or_404
from .models import Food
from .forms import FoodForm
from .forms import LoginForm
#from .forms import userregistrationform
from django.contrib.auth.models import auth
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
@login_required(login_url='login_user')
def index(request):
    return render(request,'index.html')

@login_required(login_url='login_user')
def foodEntry(request):
    if request.method == "POST":
        food_form = FoodForm(request.POST)
        if food_form.is_valid():
            food = food_form.save(commit = False)
            food.user = request.user
            food.save()
            return redirect("foodlist")
    else :
        food_form = FoodForm()    
    return render(request, 'foodentry.html',
                   {"food_form": food_form})

@login_required(login_url='login_user')
def foodlist(request):
    foods = Food.objects.all()
    return render(request,'foodlist.html',
                  {'foods':foods} )
def login_user(request):
    form = LoginForm()
    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)
            if user is not None:
                auth.login(request, user)
                return redirect('index')
            else:
                messages.error(request, 'Invalid username or password')
    context = {'loginform':form}
    
    return render(request, 'login_user.html', context=context )
def register(request):
        if request.method == 'POST':
            form = UserCreationForm(request.POST)
            if form.is_void():
                 form.save()
                 return redirect('login_user')
        else:
             form = UserCreationForm()
    
        return render(request,'register.html', {'form':form})

@login_required(login_url='login_user')
def logout_user(request):
    auth.logout(request)
    messages.success(request, ('You are now logged out..'))
    return redirect(request, '')

@login_required(login_url='login_user')
def delete_food(request,food_id):
    food = get_object_or_404(Food,id=food_id,user=request.user)
    food.delete()
    return redirect('foodlist')

@login_required(login_url='login_user')
def reset_calories(request):
    foods = Food.objects.filter(user=request.user)
    for food in foods:
        food.calories_reset = True
        food.total_calories = 0
        food.save()
    return redirect('foodlist')


       