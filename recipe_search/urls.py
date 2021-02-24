from django.urls import path
from . import views

# be clear with pattern names; reverse look-up capable
urlpatterns = [
    path('', views.home, name='recipe-search-home'),
    path('search-by-name/', views.search_by_name, name='recipe-search-food-name'),
    path('search-by-ingredient/', views.search_by_ingredient, name='recipe-search-food-ingredient'),
]
