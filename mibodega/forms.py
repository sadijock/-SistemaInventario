# hereda de form
from django import forms

class FormCategoria(forms.Form):
    codigo_Categoria = forms.IntegerField(
        label= "Codigo C",
        max_value=10,
        required=True,
        widget=forms.NumberInput(
            attrs={
               'placeholder':'Codigo C',
                'class': 'codigo_c' 
            }
        )

    )
    nombre_c = forms.CharField(
        label= "Nombre Categoria",
        max_length=20,
        required=True,
        widget=forms.TextInput(
            attrs={
                'placeholder':'Nombre Categoria',
                'class': 'nombre_c'
            }
        )
    )