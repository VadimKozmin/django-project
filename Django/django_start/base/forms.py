from .models import Soup
from django.forms import ModelForm, TextInput, NumberInput


class SoupForm(ModelForm):
    class Meta:
        model = Soup
        fields = ['title', 'count']

        widgets = {
            "title": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Блюдо'
            })
        }