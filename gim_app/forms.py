# forms.py
from django import forms
from.models import Nombre
from django import forms
from django.db.models import Q




class UsuarioForm(forms.ModelForm):
    is_admin = forms.BooleanField(required=False, label='Es administrador')
    class Meta:
        model = Nombre
        fields = ['username', 'password', 'email']
        widgets = {
            'is_admin': forms.CheckboxInput(),
    
        }

    class Meta:
        model = Nombre
        fields = ['username', 'password', 'email']
        widgets = {
            'is_admin': forms.CheckboxInput(),
        }





