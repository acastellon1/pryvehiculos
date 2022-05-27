from django import forms
from apps.vehiculos.models import TipoVehiculo


class TipoVehiculoForm(forms.ModelForm):

    class Meta:
        model = TipoVehiculo

        fields = [
            'nombre',
        ]

        labels = {
            'nombre': 'Ingrese el tipo de vehiculo',
        }

        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
        }