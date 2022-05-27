from django.shortcuts import render, redirect
from apps.vehiculos.formmarca import MarcaForm
from apps.vehiculos.formtipovehiculo import TipoVehiculoForm
from apps.vehiculos.formvehiculo import VehiculoForm
from apps.vehiculos.models import Vehiculo, Marca, TipoVehiculo
# Create your views here.

def listvehiculos(request):
    vehiculos = Vehiculo.objects.all().order_by('id')
    context = {'vehiculos': vehiculos}
    return render(request, 'vehiculos/listVehiculos.html', context)


    
def home(request):
    return render(request, 'base/base.html')

def vehiculoCreate(request):
    if request.method == 'POST':
        form = VehiculoForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('vehiculos:listVehiculos')
    else:
        form = VehiculoForm()
    return render(request, 'vehiculos/vehiculo_form.html', {'form': form})


def vehiculoEdit(request, id_vehiculo):
    
    vehiculos = Vehiculo.objects.get(pk=id_vehiculo)

    if request.method == 'GET':
        form = VehiculoForm(instance=vehiculos) #clase que importo desde el archivo formVehiculo.py
    else:
        form =VehiculoForm(request.POST, instance=vehiculos)
        if form.is_valid():
            form.save()
        
        return redirect('vehiculos:listVehiculos')
    return render(request, 'vehiculos/vehiculo_form.html', {'form': form}) 

def vehiculoElim(request, id_vehiculo):
    
    vehiculo = Vehiculo.objects.get(pk=id_vehiculo)

    if request.method == 'POST':
        vehiculo.delete() #es que se usa para eliminar un elemento de la base de datos
        return redirect('vehiculos:listVehiculos')

    return render(request,'vehiculos/vehiculoElimform.html', {'vehiculos': vehiculo})

####### Marcas #######

def listmarcas(request):
    marcas = Marca.objects.all().order_by('id')
    context = {'vehiculos': marcas}
    return render(request, 'marcas/listMarcas.html', context)


def marcaCreate(request):
    if request.method == 'POST':
        form = MarcaForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('vehiculos:listmarcas')
    else:
        form = MarcaForm()
    return render(request, 'marcas/marca_form.html', {'form': form})


def marcaEdit(request, id_marca):
    
    marcas = Marca.objects.get(pk=id_marca)

    if request.method == 'GET':
        form = MarcaForm(instance=marcas) #clase que importo desde el archivo formVehiculo.py
    else:
        form =MarcaForm(request.POST, instance=marcas)
        if form.is_valid():
            form.save()
        
        return redirect('vehiculos:listmarcas')
    return render(request, 'marcas/marca_form.html', {'form': form}) 


def marcaElim(request, id_marca):
    
    marca = Marca.objects.get(pk=id_marca)

    if request.method == 'POST':
        marca.delete() #es que se usa para eliminar un elemento de la base de datos
        return redirect('vehiculos:listmarcas')

    return render(request,'marcas/marcaElimform.html', {'marca': marca})

###### TipoVehiculo #######

def listTipoVehiculos(request):
    tipovehiculos = TipoVehiculo.objects.all().order_by('id')
    context = {'vehiculos': tipovehiculos}
    return render(request, 'tipovehiculos/listTipoVehiculos.html', context)

def tipovehiculoCreate(request):
    if request.method == 'POST':
        form = TipoVehiculoForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('vehiculos:listTipoVehiculos')
    else:
        form = TipoVehiculoForm()
    return render(request, 'tipovehiculos/tipovehiculo_form.html', {'form': form})

def tipovehiculoEdit(request, id_tipovehiculo):
    
    tipovehiculos = TipoVehiculo.objects.get(pk=id_tipovehiculo)

    if request.method == 'GET':
        form = TipoVehiculoForm(instance=tipovehiculos) #clase que importo desde el archivo formVehiculo.py
    else:
        form =TipoVehiculoForm(request.POST, instance=tipovehiculos)
        if form.is_valid():
            form.save()
        
        return redirect('vehiculos:listTipoVehiculos')
    return render(request, 'tipovehiculos/tipovehiculo_form.html', {'form': form})

def tipovehiculoElim(request, id_tipovehiculo):
    
    tipovehiculo = TipoVehiculo.objects.get(pk=id_tipovehiculo)

    if request.method == 'POST':
        tipovehiculo.delete() #es que se usa para eliminar un elemento de la base de datos
        return redirect('vehiculos:listTipoVehiculos')

    return render(request,'tipovehiculos/tipovehiculoElimform.html', {'tipovehiculo': tipovehiculo}) 

