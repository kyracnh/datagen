from django.urls import path
from . import views
from .views import generate_data
from .views import generate_data

urlpatterns = [
    path('', views.search_view, name='search'),  # The main search page
    path('results/', views.search_results, name='search_results'),  # Results page
    path('generate_data/', views.generate_data, name='generate_data'),  # Data generation
    path('result/', views.search_view, name='result_view'),  # Chart results page
    path('', views.search, name='search'),  # Main search page
    path('search_results/', views.search_results, name='search_results'), 
]