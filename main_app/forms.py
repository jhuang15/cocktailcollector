from django.forms import ModelForm
from .models import Preference

class PreferenceForm(ModelForm):
  class Meta:
    model = Preference
    fields = ['date', 'glassware']