from django import forms
from .models import Tasacion

class TasacionForm(forms.ModelForm):
    class Meta:
        model = Tasacion
        fields = ['nombre_titular', 'cuit', 'direccion', 'telefono_contacto', 'impuesto_inmobiliario', 'email']
        widgets = {
            'nombre_titular': forms.TextInput(attrs={'class': 'form-control'}),
            'cuit': forms.TextInput(attrs={'class': 'form-control'}),
            'direccion': forms.TextInput(attrs={'class': 'form-control'}),
            'telefono_contacto': forms.TextInput(attrs={'class': 'form-control'}),
            'impuesto_inmobiliario': forms.FileInput(attrs={'class': 'form-control-file'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
        }
