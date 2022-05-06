from django.urls import path
from apps.vehiculos.views import listvehiculos, vehiculoCreate

app_name= 'vehiculos'
urlpatterns = [
    path('', listvehiculos, name = 'listVehiculos'),
    path('nuevo/', vehiculoCreate, name = 'vehiculoCreate'),
]