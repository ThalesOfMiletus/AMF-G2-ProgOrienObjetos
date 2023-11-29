from django import forms
from .models import Granada

class GranadaForm(forms.ModelForm):
    class Meta:
        model = Granada
        fields = ['tipo_granada', 'bomb', 'link', 'descricao']
