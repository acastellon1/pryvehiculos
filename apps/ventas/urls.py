from django.urls import path
from apps.ventas.views import VehiculoVentaCreate, VehiculoVentaEdit, VehiculoVentaElim, consulta1, consulta2, consulta3, consulta4, listVehiculoVenta, listVentas, ventaCreate, ventaEdit, ventaElim



app_name = 'ventas'
urlpatterns = [
    path('', listVentas, name='listVentas'),
    path('nuevo/', ventaCreate, name = 'ventaCreate'),
    path('actualizar/<int:id_venta>/', ventaEdit, name='ventaEdit'),
    path('eliminar/<int:id_venta>/', ventaElim, name='ventaElim'),

    ##### VehiculoVenta ######
    path('vehiculoventa', listVehiculoVenta, name='listVehiculoVenta'),
    path('nuevav/', VehiculoVentaCreate, name = 'VehiculoVentaCreate'),
    path('actualizarvv/<int:id_vehiculoventa>/', VehiculoVentaEdit, name='VehiculoVentaEdit'),
    path('eliminarvv/<int:id_vehiculoventa>/', VehiculoVentaElim, name='VehiculoVentaElim'),

    ###### consultas ######

    path('consulta1/', consulta1, name='consulta1'),
    path('consulta2/', consulta2, name='consulta2'),
    path('consulta3/', consulta3, name='consulta3'),
    path('consulta4/', consulta4, name='consulta4'),


    
]