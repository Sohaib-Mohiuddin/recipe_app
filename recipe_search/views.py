from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from py_edamam import PyEdamam

# Create your views here.
edamam_conn = PyEdamam(recipes_appid='3281df5a', recipes_appkey='d8593ef2bf3fe138d042e548796c986a')

users = [
	{
		'name': 'sohaib',
		'username': 'sm',
		'date': '2018-27-08'
	},
	{
		'name': 'user2',
		'username': 'userdsfds',
		'date': '2020-27-08'
	}
]

# class HomepageView(TemplateView):
# 	template_name = "home.html"

def home(request):
	context = {
		'users':users
	}
	return render(request, 'recipe_search/home.html', context)

def search_by_name(request):
	return render(request, 'recipe_search/searchbyname.html')

def search_by_ingredient(request):
	return render(request, 'recipe_search/searchbyingredient.html')