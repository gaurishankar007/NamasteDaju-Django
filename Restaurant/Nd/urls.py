from django.urls import path
from . import views

urlpatterns = [
    path('home', views.home),
    path('menu', views.menu),
    path('gallery', views.gallery),
    path('stories', views.stories),
    path('reservation', views.reservation),
    path('catering', views.catering),
    path('contact', views.contact),
]