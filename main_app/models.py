from django.db import models

# Create your models here.
class Cocktail(models.Model):
  name = models.CharField(max_length=100)
  type = models.CharField(max_length=100)
  description = models.TextField(max_length=300)
  difficulty = models.IntegerField()

  def __str__(self):
    return self.name