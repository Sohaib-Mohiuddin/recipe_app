from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from py_edamam import PyEdamam

# Create your views here.


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
	query=None
	search_results = []
	if request.method == "GET":
		edamam_conn = PyEdamam(recipes_appid='3281df5a', recipes_appkey='d8593ef2bf3fe138d042e548796c986a')
		query = request.GET.get('searchRecipe')
		search_results = edamam_conn.search_recipe(query)
	
	return render(request, 'recipe_search/searchbyname.html', {'query' : query,
											'search_results' : search_results})

def search_by_ingredient(request):
	return render(request, 'recipe_search/searchbyingredient.html')

