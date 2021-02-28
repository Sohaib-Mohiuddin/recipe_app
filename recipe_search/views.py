from django.shortcuts import render, HttpResponse
from django.views.generic import TemplateView, ListView
from py_edamam import PyEdamam, Edamam

# Create your views here.
user_ip = 'User'
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

def visitor_ip_address(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')

    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip

def home(request):
	user_ip = visitor_ip_address(request)
	# print(request.META)
	context = {}
	context['users'] = users
	context['user_ip'] = user_ip
	return render(request, 'recipe_search/home.html', context)

def search_by_name(request):
	context = {}
	if request.method == "GET":
		edamam_conn = PyEdamam(recipes_appid='3281df5a', recipes_appkey='d8593ef2bf3fe138d042e548796c986a')
		context['query'] = request.GET.get('searchRecipe')
		context['search_results'] = edamam_conn.search_recipe(context['query'])
	return render(request, 'recipe_search/searchbyname.html', context)

def search_by_ingredient(request):
	context = {}
	if request.method == "GET":
		edamam_conn_ingr = Edamam(food_appid='b4b4db31', food_appkey='1175509923bd6485f3e5f3fc8b88c596')
		context['query_ingr'] = request.GET.get('searchIngredient')
		context['search_results_ingr'] = edamam_conn_ingr.search_food(context['query_ingr'])
	return render(request, 'recipe_search/searchbyingredient.html', context)

