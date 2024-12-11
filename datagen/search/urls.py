from django.urls import path
from . import views

urlpatterns = [
    path('', views.search_view, name='search'),
    path('results/', views.search_results, name='search_results'),
]