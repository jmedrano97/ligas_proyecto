from django.forms import ModelForm
from .models import Equipo, Jugador
from django import forms

class EquipoForm(ModelForm):
    class Meta:
        model = Equipo
        fields = ['nombre','telefono','liga','escudo_img']
        widgets = {
            'nombre': forms.TextInput(attrs={'class':'form-control','placeholder': 'Ingresa el nombre del equipo'}),
            'telefono': forms.TextInput(attrs={'class':'form-control','placeholder': 'Ingresa el telefono del equipo'}),
            'liga': forms.Select(attrs={'class':'form-control'}),
            'escudo_img': forms.FileInput(attrs={'class':'form-control-file'}),
        }

class JugadorForm(ModelForm):
    class Meta:
        model = Jugador
        fields = ['nombre','telefono','fecha_nacimiento','ocupacion','numero_playera','equipo','liga','jugador_img','identificacion_img']
        widgets = {
            'nombre': forms.TextInput(attrs={'class':'form-control','placeholder': 'Campo obligatorio*'}),
            'telefono': forms.TextInput(attrs={'class':'form-control','placeholder': ''}),
            'fecha_nacimiento': forms.DateInput(attrs={'class': 'form-control', 'placeholder': 'Campo obligatorio*', 'type': 'date'}),
            'ocupacion': forms.Select(attrs={'class':'form-control'}),
            'numero_playera': forms.NumberInput(attrs={'class':'form-control','placeholder': ''}),
            'equipo': forms.Select(attrs={'class':'form-control'}),
            'liga': forms.Select(attrs={'class':'form-control'}),
            'jugador_img': forms.FileInput(attrs={'class':'form-control-file'}),
            'identificacion_img': forms.FileInput(attrs={'class':'form-control-file'}),
        }