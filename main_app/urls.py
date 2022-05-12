from django.urls import path
from . import views

urlpatterns = [
  path('', views.home, name='home'),
  path('about/', views.about, name='about'),
  path('cocktails/', views.cocktails_index, name='index'),
  path('cocktails/<int:cocktail_id>/', views.cocktails_detail, name='detail'),
]