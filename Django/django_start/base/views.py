from django.shortcuts import render, redirect
from .models import Soup, Second_dish, Salad, Drinks
from .forms import SoupForm


def menu_home(request):
    second_dish = Second_dish.objects.all()
    soup = Soup.objects.all()
    salad = Salad.objects.all()
    drinks = Drinks.objects.all()
    return render(request, 'base/lunch.html', {'second_dish': second_dish, 'soup': soup, 'salad': salad,
                                               'drinks': drinks})


def create(request):
    if request.method == 'POST':
        form = SoupForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('create')

    form = SoupForm()
    data = {'form': form}
    return render(request, 'base/create_main.html', data)

