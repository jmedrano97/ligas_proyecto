from django.forms import ModelForm
from .models import Equipo, Jugador, Contacto
from django import forms

class EquipoForm(ModelForm):
    class Meta:
        model = Equipo
        fields = ['nombre','telefono','escudo_img']
        widgets = {
            'nombre': forms.TextInput(attrs={'class':'form-control','placeholder': 'Ingresa el nombre del equipo'}),
            'telefono': forms.TextInput(attrs={'class':'form-control','placeholder': 'Ingresa el telefono del equipo'}),
            'escudo_img': forms.FileInput(attrs={'class':'form-control-file'}),
        }

class JugadorForm(ModelForm):
    class Meta:
        model = Jugador
        fields = ['nombre','telefono','fecha_nacimiento','ocupacion','numero_playera','equipo','jugador_img','identificacion_img']
        widgets = {
            'nombre': forms.TextInput(attrs={'class':'form-control','placeholder': 'Campo obligatorio*'}),
            'telefono': forms.TextInput(attrs={'class':'form-control','placeholder': ''}),
            'fecha_nacimiento': forms.DateInput(attrs={'class': 'form-control', 'placeholder': 'Campo obligatorio*', 'type': 'date'}),
            'ocupacion': forms.Select(attrs={'class':'form-control'}),
            'numero_playera': forms.NumberInput(attrs={'class':'form-control','placeholder': ''}),
            'equipo': forms.Select(attrs={'class':'form-control'}),
            'jugador_img': forms.FileInput(attrs={'class':'form-control-file'}),
            'identificacion_img': forms.FileInput(attrs={'class':'form-control-file'}),
        }

class ContactoForm(ModelForm):
    class Meta:
        model = Contacto
        fields = ['nombre','email','telefono','mensaje']
        widgets = {
            'nombre': forms.TextInput(attrs={'class':'form-control','placeholder': 'Campo obligatorio*'}),
            'email': forms.EmailInput(attrs={'class':'form-control','placeholder': 'Campo obligatorio*'}),
            'telefono': forms.TextInput(attrs={'class':'form-control','placeholder': ''}),
            'mensaje': forms.Textarea(attrs={'class':'form-control','placeholder': ''}),
        }