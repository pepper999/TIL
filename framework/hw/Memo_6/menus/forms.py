from django import forms
from .models import Menu

# Create your models here.
class MenuForm(forms.ModelForm):
    class Meta:
        model = Menu
        fields = '__all__'