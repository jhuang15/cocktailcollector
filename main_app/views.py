from django.shortcuts import render,redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from .models import Cocktail, Ingredient
from .forms import PreferenceForm


def home(request):
  return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')

def cocktails_index(request):
  cocktails = Cocktail.objects.all()
  return render(request, 'cocktails/index.html', { 'cocktails': cocktails })

def cocktails_detail(request, cocktail_id):
  cocktail = Cocktail.objects.get(id=cocktail_id)
  id_list = cocktail.ingredients.all().values_list('id')
  ingredients_cocktail_doesnt_have = Ingredient.objects.exclude(id__in=id_list)
  preference_form = PreferenceForm()
  return render(request, 'cocktails/detail.html', { 
    'cocktail': cocktail, 
    'preference_form': preference_form,
    'ingredients': ingredients_cocktail_doesnt_have
  })

class CocktailCreate(CreateView):
  model = Cocktail
  fields = ['name', 'type', 'description', 'difficulty']
  

class CocktailUpdate(UpdateView):
  model = Cocktail
  fields = ['type', 'description', 'difficulty']

class CocktailDelete(DeleteView):
  model = Cocktail
  success_url = '/cocktails/'

def add_preference(request, cocktail_id):
  form = PreferenceForm(request.POST)
  if form.is_valid():
    new_preference = form.save(commit=False)
    new_preference.cocktail_id = cocktail_id
    new_preference.save()
  return redirect('detail', cocktail_id=cocktail_id)

def assoc_ingredient(request, cocktail_id, ingredient_id):
  Cocktail.objects.get(id=cocktail_id).ingredients.add(ingredient_id)
  return redirect('detail', cocktail_id=cocktail_id)

def unassoc_ingredient(request, cocktail_id, ingredient_id):
  Cocktail.objects.get(id=cocktail_id).ingredients.remove(ingredient_id)
  return redirect('detail', cocktail_id=cocktail_id)

class IngredientList(ListView):
  model = Ingredient

class IngredientDetail(DetailView):
  model = Ingredient

class IngredientCreate(CreateView):
  model = Ingredient
  fields = '__all__'

class IngredientUpdate(UpdateView):
  model = Ingredient
  fields = ['name', 'unit']

class IngredientDelete(DeleteView):
  model = Ingredient
  success_url = '/ingredients/'