from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from py_edamam import PyEdamam, Edamam

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
		print(search_results)
	return render(request, 'recipe_search/searchbyname.html', {'query' : query,
											'search_results' : search_results})

def search_by_ingredient(request):
	query_ingr=None
	search_results_ingr = []
	if request.method == "GET":
		edamam_conn_ingr = Edamam(food_appid='b4b4db31', food_appkey='1175509923bd6485f3e5f3fc8b88c596')
		query_ingr = request.GET.get('searchIngredient')
		search_results_ingr = edamam_conn_ingr.search_food(query_ingr)
		# print(search_results_ingr)
	return render(request, 'recipe_search/searchbyingredient.html', {'query_ingr' : query_ingr,
											'search_results_ingr' : search_results_ingr})

