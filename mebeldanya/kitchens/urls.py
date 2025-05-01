from django.urls import path
from . import views

urlpatterns = [
    path('', views.kitchen_list, name='kitchen_list'),
    path('catalog/', views.catalog, name='catalog'),
    path('about/', views.about, name='about'),
    path('contacts/', views.contacts, name='contacts'),
    path('reviews/', views.reviews, name='reviews'),
]
