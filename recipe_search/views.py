from django.shortcuts import render, HttpResponse
from django.views.generic import TemplateView, ListView
from django.contrib.auth.decorators import login_required
from py_edamam import PyEdamam, Edamam
from .models import SavedList
# from users.forms import SavedListForm

def home(request):
	return render(request, 'recipe_search/home.html')

@login_required
def search_by_name(request):
	context = {}
	if request.method == "GET":
		edamam_conn = PyEdamam(recipes_appid='3281df5a', recipes_appkey='d8593ef2bf3fe138d042e548796c986a')
		context['query'] = request.GET.get('searchRecipe')
		context['search_results'] = edamam_conn.search_recipe(context['query'])
	return render(request, 'recipe_search/searchbyname.html', context)

@login_required
def search_by_ingredient(request):
	context = {}
	if request.method == "GET":
		edamam_conn_ingr = Edamam(food_appid='b4b4db31', food_appkey='1175509923bd6485f3e5f3fc8b88c596')
		context['query_ingr'] = request.GET.get('searchIngredient')
		context['search_results_ingr'] = edamam_conn_ingr.search_food(context['query_ingr'])
	return render(request, 'recipe_search/searchbyingredient.html', context)

@login_required
def saved_ingredient_list(request):
	context = {}
	user = request.user
	saved_list = SavedList.objects.get(user=user).saved_list
	altered_list = list(saved_list.split(','))
	context['saved_list'] = altered_list
	return render(request, 'recipe_search/savedlist.html', context)

# TODO 2 FIX ADD TO LIST FEATURE
# @login_required
# def add_to_list(request):
# 	user = request.user
# 	saved_list = SavedList.objects.get(user=user).saved_list
# 	form = SavedListForm(request.POST, instance=update_list)
# 	if form.is_valid():
# 		form.save()
# 		return render(request, 'recipe_search/searchbyingredient.html', context)