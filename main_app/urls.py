from django.urls import path
from . import views

urlpatterns = [
  path('', views.home, name='home'),
  path('about/', views.about, name='about'),
  path('cocktails/', views.cocktails_index, name='index'),
  path('cocktails/<int:cocktail_id>/', views.cocktails_detail, name='detail'),
  path('cocktails/create/', views.CocktailCreate.as_view(), name='cocktails_create'),
  path('cocktails/<int:pk>/update/', views.CocktailUpdate.as_view(), name='cocktails_update'),
  path('cocktails/<int:pk>/delete/', views.CocktailDelete.as_view(), name='cocktails_delete'),
  path('cocktailss/<int:cocktail_id>/add_preference/', views.add_preference, name='add_preference'),
  path('cocktails/<int:cocktail_id>/assoc_ingredient/<int:ingredient_id>/', views.assoc_ingredient, name='assoc_ingredient'),
  path('cocktails/<int:cocktail_id>/unassoc_ingredient/<int:ingredient_id>/', views.unassoc_ingredient, name='unassoc_ingredient'),
  path('ingredients/', views.IngredientList.as_view(), name='ingredients_index'),
  path('ingredients/<int:pk>/', views.IngredientDetail.as_view(), name='ingredients_detail'),
  path('ingredients/create/', views.IngredientCreate.as_view(), name='ingredients_create'),
  path('ingredients/<int:pk>/update/', views.IngredientUpdate.as_view(), name='ingredients_update'),
  path('ingredients/<int:pk>/delete/', views.IngredientDelete.as_view(), name='ingredients_delete'),
]
