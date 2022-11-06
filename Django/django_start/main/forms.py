from .models import Main_menu, Author, Author_drinks, Coffee, Coctails, Dessert, Main, Rus, Salad, Tea, Water, Juice, \
    Carbon, Soup
from django.forms import ModelForm, TextInput, NumberInput


class Main_menuForm(ModelForm):
    class Meta:
        model = Main_menu
        fields = ['title', 'count']

        widgets = {
            "title": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Блюдо'
            }),
            'count': NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Цена'
            })
        }
