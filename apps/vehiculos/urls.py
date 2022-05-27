from django.urls import path
from apps.vehiculos.views import listTipoVehiculos, listmarcas, listvehiculos, marcaEdit, marcaElim, tipovehiculoCreate, tipovehiculoEdit, tipovehiculoElim, vehiculoCreate, vehiculoEdit, vehiculoElim, marcaCreate

app_name= 'vehiculos'
urlpatterns = [
    path('', listvehiculos, name = 'listVehiculos'),
    path('nuevo/', vehiculoCreate, name = 'vehiculoCreate'),
    path('actualizar/<int:id_vehiculo>/', vehiculoEdit, name='vehiculoEdit'),
    path('eliminar/<int:id_vehiculo>/', vehiculoElim, name='vehiculoElim'),

    #Marca
    path('marcas', listmarcas, name='listmarcas'),
    path('nuevam/', marcaCreate, name = 'marcaCreate'),
    path('actmarca/<int:id_marca>/', marcaEdit, name='marcaEdit'),
    path('eliminarm/<int:id_marca>/', marcaElim, name='marcaElim'),

    #TipoVehiculo
    path('tipovehiculos', listTipoVehiculos, name='listTipoVehiculos'),
    path('nuevotp/', tipovehiculoCreate, name = 'tipovehiculoCreate'),
    path('acttipovehiculo/<int:id_tipovehiculo>/', tipovehiculoEdit, name='tipovehiculoEdit'),
    path('eliminartp/<int:id_tipovehiculo>/', tipovehiculoElim, name='tipovehiculoElim'),


    
]