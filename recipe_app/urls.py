"""recipe_app URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from users import views as users_views
from recipe_search import views as recipe_search_views
from django.contrib.auth import views as login_out_views

"""
''          	- route to recipe-search app
admin/			- route to django administrative services
"""
urlpatterns = [
	path('admin/', admin.site.urls),
    # path('', include('recipe_search.urls')),
    # /users urls
    path('register/', users_views.register, name='recipe-search-register'),
    path('login/', login_out_views.LoginView.as_view(template_name='users/login.html'), name='recipe-search-login'),
    path('logout/', login_out_views.LogoutView.as_view(template_name='users/logout.html'), name='recipe-search-logout'),

    # /recipe_search urls
    path('', recipe_search_views.home, name='recipe-search-home'),
    path('search-by-name/', recipe_search_views.search_by_name, name='recipe-search-food-name'),
    path('search-by-ingredient/', recipe_search_views.search_by_ingredient, name='recipe-search-food-ingredient'),
    path('saved-ingredient-list/', recipe_search_views.saved_ingredient_list, name='recipe-search-saved-list'),
]
