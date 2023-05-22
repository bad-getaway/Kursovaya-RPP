from multiprocessing import context
from django.shortcuts import render, redirect
from . import models
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .forms import CreateUserForm
import requests
from rest_framework import generics
from .serializers import OrderSerializers, GameSerializers, CategorySerializers


# Create your views here.

def home(request):

    context = {
        
    }
    return render(request, 'mainSite/home.html', context)

def catalog(request):
    category = models.Category.objects.all()

    context = {
        'category':category,

    }
    return render(request, 'mainSite/catalog.html', context) 

def choose_category(request, pk):
    games = models.Games.objects.filter(category=pk)
    category = models.Category.objects.get(id=pk)
    context = {
        'games':games,
        'category':category,
        
    }

    print(context)
    return render(request, 'mainSite/choose_category.html', context) 

def choose_product(request, pk):
    games = models.Games.objects.get(pk=pk)
    order = models.Order.objects.filter(games=games, user=request.user)
  
    context = {
        'games':games,
        'order':order,

    }
    return render(request, 'mainSite/choose_product.html', context) 


@login_required(login_url='/login_page')
def make_order(request, pk):
    user = request.user
    games = models.Games.objects.get(id=pk)
    if request.method == 'POST':
        order = models.Order.objects.create(
                    user = user,
                    games = games,
                    phone = request.POST.get('phone'),
                 
                    )
       



        return redirect('game_pass')

    context = {
        'games':games
    }
    return render(request, 'mainSite/make_order.html', context)

def game_pass(request):
    order_info = models.Order.objects.filter(user=request.user).all().last()
    game_info = models.Games.objects.get(id=order_info.games.id)


    context = {
        'order_info':order_info,
        'game_info':game_info,
    }
    return render(request, 'mainSite/game_pass.html', context)

def register(request):
    user_form = CreateUserForm

    if request.method == 'POST':
        user_form = CreateUserForm(request.POST)
        if user_form.is_valid():
                user_form.save()
                username = request.POST.get('username')
                password = request.POST.get('password1')
                user = authenticate(request, username=username, password=password)
                login(request,user)

                return redirect('home')

    context = {
        'user_form':user_form,
    }

    return render(request, 'mainSite/register.html', context)



def login_page(request):
    error = ''
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            error = 'Проверьте введёные данные!'

    context = {
        "error":error,

    }
    return render(request, 'mainSite/login.html', context)



def logout_view(request):
    logout(request)
    return redirect('home')


class OrderListView(generics.ListAPIView):
    serializer_class = OrderSerializers
    queryset = models.Order.objects.all()


class CategoryListView(generics.ListAPIView):
    serializer_class = CategorySerializers
    queryset = models.Category.objects.all()


class GameListView(generics.ListAPIView):
    serializer_class = GameSerializers
    queryset = models.Games.objects.all()

class OrderCreateView(generics.CreateAPIView):
    serializer_class = OrderSerializers