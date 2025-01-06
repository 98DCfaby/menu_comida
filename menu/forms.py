from django import forms
from .models import Platillo

class PlatilloForm(forms.ModelForm):
    class Meta:
        model = Platillo
        fields = ['nombre', 'descripcion', 'informacion_nutricional', 'fecha']
        widgets = {
            'fecha': forms.DateInput(attrs={'type': 'date'})  # Usa un calendario para seleccionar la fecha
        }
