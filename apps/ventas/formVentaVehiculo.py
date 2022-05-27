from django import forms
from apps.ventas.models import VehiculoVenta


class VehiculoVentaForm(forms.ModelForm):

    class Meta:
        model = VehiculoVenta

        fields = [
            'vehiculo',
            'venta',
            'cantidad',
            'precio',
            
        ]

        labels = {
            'vehiculo': 'Seleccione el vehiculo',
            'venta': 'Seleccione la venta',
            'cantidad': 'Ingrese la cantidad',
            'precio': 'Ingrese el precio',
            
        }

        widgets = {
            'vehiculo': forms.Select(attrs={'class': 'form-control'}),
            'venta': forms.Select(attrs={'class': 'form-control'}),
            'cantidad': forms.TextInput(attrs={'class': 'form-control'}),
            'precio': forms.TextInput(attrs={'class': 'form-control'}),
        }