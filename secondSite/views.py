from django.shortcuts import render
import requests

# Create your views here.
def home(request):

    response = requests.get('http://127.0.0.1:8000/api/v1/order_all')
    order_info = response.json()

    response = requests.get('http://127.0.0.1:8000/api/v1/game_all')
    game_info = response.json()

    response = requests.get('http://127.0.0.1:8000/api/v1/category_all')
    category = response.json()

    context = {
        'order_info':order_info,
        'game_info':game_info,
        'category':category,
        
    }
    return render(request, 'secondSite/home.html', context)

def admin_home(request):

    response = requests.get('http://127.0.0.1:8000/api/v1/order_all')
    order_info = response.json()

    response = requests.get('http://127.0.0.1:8000/api/v1/game_all')
    game_info = response.json()

    response = requests.get('http://127.0.0.1:8000/api/v1/category_all')
    category = response.json()

    context = {
        'order_info':order_info,
        'game_info':game_info,
        'category':category,
        
    }
    return render(request, 'secondSite/adminhome.html', context)


def game(request, pk):

    response = requests.get('http://127.0.0.1:8000/api/v1/order_all')
    order_info = response.json()

    response = requests.get('http://127.0.0.1:8000/api/v1/game_all')
    game_info = response.json()

    response = requests.get('http://127.0.0.1:8000/api/v1/category_all')
    category = response.json()

    context = {
        'order_info':order_info,
        'game_info':game_info,
        'category':category,
        'game_pk':pk,
        
    }
    return render(request, 'secondSite/game.html', context)


def admingame(request, pk):

    response = requests.get('http://127.0.0.1:8000/api/v1/order_all')
    order_info = response.json()

    response = requests.get('http://127.0.0.1:8000/api/v1/game_all')
    game_info = response.json()

    response = requests.get('http://127.0.0.1:8000/api/v1/category_all')
    category = response.json()

    context = {
        'order_info':order_info,
        'game_info':game_info,
        'category':category,
        'order_pk':pk,
        
    }
    return render(request, 'secondSite/admingame.html', context)