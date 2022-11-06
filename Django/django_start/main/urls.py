from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_page, name='home_page'),
    path('main_menu', views.main_menu, name='main_menu'),
    path('business', views.business, name='business'),
    path('contacts', views.contacts, name='contacts'),
    path('create', views.create, name='create')
]