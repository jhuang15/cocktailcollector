from django.shortcuts import render
# Add the following import
from django.http import HttpResponse

class Cocktail:  # Note that parens are optional if not inheriting from another class
  def __init__(self, name, type, description):
    self.name = name
    self.type = type
    self.description = description

cocktails = [
  Cocktail('Mojito', 'Rum', 'Mojito is a traditional Cuban highball. The cocktail often consists of five ingredients: white rum, sugar, lime juice, soda water, and mint.'),
  Cocktail('Nigroni', 'Gin', 'A Negroni is an Italian cocktail, made of one part gin, one part vermouth rosso and one part Campari, garnished with orange peel.'),
  Cocktail('Lemon drop', 'Vodka', 'A lemon drop is a vodka-based cocktail that has a lemony, sweet and sour flavor, prepared using lemon juice, triple sec and simple syrup.')
]

# Define the home view
def home(request):
  return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')

def cocktails_index(request):
  return render(request, 'cocktails/index.html', { 'cocktails': cocktails })