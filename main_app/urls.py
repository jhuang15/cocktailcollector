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
]