from django.forms import ModelForm
from .models import Equipo
from django import forms

class EquipoForm(ModelForm):
    class Meta:
        model = Equipo
        fields = ['nombre','liga','escudo_img']
        widgets = {
            'nombre': forms.TextInput(attrs={'class':'form-control','placeholder': 'Ingresa el nombre del equipo'}),
            'liga': forms.Select(attrs={'class':'form-control'}),
            'escudo_img': forms.FileInput(attrs={'class':'form-control-file'}),
        }