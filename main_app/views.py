from django.shortcuts import render,redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Cocktail
from .forms import PreferenceForm

# Define the home view
def home(request):
  return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')

def cocktails_index(request):
  cocktails = Cocktail.objects.all()
  return render(request, 'cocktails/index.html', { 'cocktails': cocktails })

def cocktails_detail(request, cocktail_id):
  cocktail = Cocktail.objects.get(id=cocktail_id)
  preference_form = PreferenceForm()
  return render(request, 'cocktails/detail.html', { 
    'cocktail': cocktail, 'preference_form': preference_form
  })

def add_preference(request, cocktail_id):
  form = PreferenceForm(request.POST)
  if form.is_valid():
    new_preference = form.save(commit=False)
    new_preference.cocktail_id = cocktail_id
    new_preference.save()
  return redirect('detail', cocktail_id=cocktail_id)


class CocktailCreate(CreateView):
  model = Cocktail
  fields = '__all__'
  success_url = '/cocktails/'

class CocktailUpdate(UpdateView):
  model = Cocktail
  fields = ['type', 'description', 'difficulty']

class CocktailDelete(DeleteView):
  model = Cocktail
  success_url = '/cocktails/'