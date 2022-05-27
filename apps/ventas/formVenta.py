from django import forms
from apps.ventas.models import Venta


class VentaForm(forms.ModelForm):

    class Meta:
        model = Venta

        fields = [
            'fecha',
            'valorTotal',
            'tipoPago',
            'user',
            
        ]

        labels = {
            'fecha': 'Ingrese la fecha',
            'valorTotal': 'Ingrese el valor total',
            'tipoPago': 'Ingrese el tipo de pago',
            'user': 'Seleccione el usuario',
            
        }

        widgets = {
            'fecha': forms.TextInput(attrs={'class': 'form-control'}),
            'valorTotal': forms.TextInput(attrs={'class': 'form-control'}),
            'tipoPago': forms.TextInput(attrs={'class': 'form-control'}),
            'user': forms.Select(attrs={'class': 'form-control'}),
            
        }