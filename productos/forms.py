from django import forms
from .models import Producto, Venta

class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = [
            'id',
            'nombre',
            'cantidad',
            'valor',
            'unidad',
            'tipo',


        ]

        labels = {

        'id' : 'Id',
        'nombre': 'Nombre',
        'cantidad': 'Cantidad',
        'valor':'Valor',
        'unidad':'Unidad',
        'tipo':'Tipo',


        }

class VentaForm(forms.ModelForm):
    class Meta:
        model = Venta
        fields = [
            'producto',
        ]
        labels = {
            'producto': 'Producto',
        }
