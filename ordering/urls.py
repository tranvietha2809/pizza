from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('pizza', views.pizza, name="pizza"),
    path('pizza/add_pizza', views.add_pizza, name="add_pizza"),
    path('get_pizza_price/', views.get_pizza_price, name="get_pizza_price"),
    path('subs', views.subs, name="subs"),
    path("subs/add_subs", views.add_subs, name="add_subs"),
    path('get_subs_price/', views.get_subs_price, name="get_subs_price"),
    path("salads", views.salads, name="salads"),
    path('salads/add_salads', views.add_salads, name="add_salads"),
    path('get_salads_price/', views.get_salads_price, name="get_salads_price"),
    path("platters", views.platters, name="platters"),
    path('platters/add_platters', views.add_platters, name="add_platters"),
    path('get_platters_price/', views.get_platters_price, name="get_platters_price")
]