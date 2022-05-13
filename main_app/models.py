from django.db import models
from django.urls import reverse
from datetime import date

GLASSWARES = (
  ('M','Martini'),
  ('R','Rocks'),
  ('H','Highball'),
  ('C','Coupe'),
  ('N','Nick&Nora')
)

class Ingredient(models.Model):
  name = models.CharField(max_length=50)
  unit = models.CharField(max_length=20)

  def __str__(self):
    return self.name

  def get_absolute_url(self):
    return reverse('ingredients_detail', kwargs={'pk': self.id})

class Cocktail(models.Model):
  name = models.CharField(max_length=100)
  type = models.CharField(max_length=100)
  description = models.TextField(max_length=300)
  difficulty = models.IntegerField()
  ingredients = models.ManyToManyField(Ingredient)

  def __str__(self):
    return self.name

  def get_absolute_url(self):
    return reverse('detail', kwargs={'cocktail_id': self.id})

  def fed_for_today(self):
    return self.preference_set.filter(date=date.today()).count() >= len(GLASSWARES)

class Preference(models.Model):
  date = models.DateField('preference date')
  glassware = models.CharField(
    max_length=1,
    choices=GLASSWARES,
    default=GLASSWARES[0][0]
    )

  cocktail = models.ForeignKey(Cocktail, on_delete=models.CASCADE)

  def __str__(self):
    return f"{self.get_glassware_display()} on {self.date}"

  class Meta:
    ordering = ['-date']