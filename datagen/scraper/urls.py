from django.urls import path
from . import views

urlpatterns = [
    path('', views.search_google, name='search_google'),
    path('competitors/', views.search_google, name='search_google'),
]
