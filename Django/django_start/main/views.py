from django.http import HttpResponse
from django.shortcuts import render
from .models import Main_menu, Author, Author_drinks, Coffee, Coctails, Dessert, Main, Rus, Salad, Tea, Water, Juice, \
    Carbon, Soup
from .forms import Main_menuForm
from django.shortcuts import render, redirect


def home_page(request):
    return render(request, 'main/home_page.html')


def main_menu(request):
    snacks = Main_menu.objects.all()
    salad = Salad.objects.all()
    rus = Rus.objects.all()
    soup = Soup.objects.all()
    main = Main.objects.all()
    dessert = Dessert.objects.all()
    coffee = Coffee.objects.all()
    tea = Tea.objects.all()
    water = Water.objects.all()
    juice = Juice.objects.all()
    carbon = Carbon.objects.all()
    author = Author.objects.all()
    drinks = Author_drinks.objects.all()
    coctails = Coctails.objects.all()
    return render(request, 'main/main_menu.html', {'snacks': snacks, 'salad': salad, 'rus': rus, 'soup': soup,
                                                   'main': main, 'dessert': dessert, 'coffee': coffee, 'tea': tea,
                                                   'water': water, 'juice': juice, 'carbon': carbon, 'author': author,
                                                   'drinks': drinks, 'coctails': coctails})


def business(request):
    return render(request, 'main/lunch.html')


def contacts(request):
    return render(request, 'main/contacts.html')


def create(request):
    if request.method == 'POST':
        form = Main_menuForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('create')

    form = Main_menuForm()
    data = {'form': form}
    return render(request, 'main/create_main.html', data)