from django import forms
from .models import contacto

class contactoForm(forms.ModelForm):
    class Meta:
        model = contacto
        fields = '__all__'