from django.shortcuts import render, redirect
from apps.ventas.formVenta import VentaForm
from apps.ventas.formVentaVehiculo import VehiculoVentaForm
from apps.ventas.models import VehiculoVenta, Venta
from django.db.models import Sum

# Create your views here.


def listVentas(request):
    ventas = Venta.objects.all().order_by('id')
    context = {'ventas' : ventas }
    return render(request, 'ventas/listVentas.html', context)

def ventaCreate(request):
    if request.method == 'POST':
        form = VentaForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('ventas:listVentas')
    else:
        form = VentaForm()
    return render(request, 'ventas/venta_form.html', {'form': form})

def ventaEdit(request, id_venta):
    
    ventas = Venta.objects.get(pk=id_venta)

    if request.method == 'GET':
        form = VentaForm(instance=ventas) #clase que importo desde el archivo formVehiculo.py
    else:
        form =VentaForm(request.POST, instance=ventas)
        if form.is_valid():
            form.save()
        
        return redirect('ventas:listVentas')
    return render(request, 'ventas/venta_form.html', {'form': form}) 

def ventaElim(request, id_venta):
    
    venta = Venta.objects.get(pk=id_venta)

    if request.method == 'POST':
        venta.delete() #es que se usa para eliminar un elemento de la base de datos
        return redirect('ventas:listVentas')

    return render(request,'ventas/ventaElimform.html', {'ventas': venta})

####### VehiculoVenta ########

def listVehiculoVenta(request):
    vehiculoventas = VehiculoVenta.objects.all().order_by('id')
    context = {'ventas' : vehiculoventas }
    return render(request, 'vehiculoventas/listVehiculoventas.html', context)

def VehiculoVentaCreate(request):
    if request.method == 'POST':
        form = VehiculoVentaForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('ventas:listVehiculoVenta')
    else:
        form = VehiculoVentaForm()
    return render(request, 'vehiculoventas/vehiculoventa_form.html', {'form': form})

def VehiculoVentaEdit(request, id_vehiculoventa):
    
    vehiculoventas = VehiculoVenta.objects.get(pk=id_vehiculoventa)

    if request.method == 'GET':
        form = VehiculoVentaForm(instance=vehiculoventas) #clase que importo desde el archivo formVehiculo.py
    else:
        form =VehiculoVentaForm(request.POST, instance=vehiculoventas)
        if form.is_valid():
            form.save()
        
        return redirect('ventas:listVehiculoVenta')
    return render(request, 'vehiculoventas/vehiculoventa_form.html', {'form': form})

def VehiculoVentaElim(request, id_vehiculoventa):
    
    vehiculoventa = VehiculoVenta.objects.get(pk=id_vehiculoventa)

    if request.method == 'POST':
        vehiculoventa.delete() #es que se usa para eliminar un elemento de la base de datos
        return redirect('ventas:listVehiculoVenta')

    return render(request,'vehiculoventas/vehiculoventaElimform.html', {'ventas': vehiculoventa})

######## Consultas #########

def consulta1(request):
    fecha1 = request.POST.get('fecha1')
    fecha2 = request.POST.get('fecha2')
    consulta1=Venta.objects.filter(fecha__range=[fecha1,fecha2]).aggregate(Sum('valorTotal'))
    
    context = {
        'fecha1': fecha1,
        'fecha2': fecha2,
        'consulta1': consulta1,
    }
    print(consulta1)
    return render(request,'consultas/consulta1.html',{'context':context})

def consulta2(request):
    fecha1 = request.POST.get('fecha1')
    fecha2 = request.POST.get('fecha2')
  
    consulta2=Venta.objects.values('fecha').filter(fecha__range=[fecha1,fecha2]).annotate(total=Sum('valorTotal'))
    
    return render(request,'consultas/consulta2.html',{'consulta2':consulta2})

def consulta3(request):
    fecha1 = request.POST.get('fecha1')
    fecha2 = request.POST.get('fecha2')
  
    consulta3=Venta.objects.values('tipoPago').filter(fecha__range=[fecha1,fecha2]).annotate(total=Sum('valorTotal'))
    
    return render(request,'consultas/consulta3.html',{'consulta3':consulta3})

def consulta4(request):
    fecha1 = request.POST.get('fecha1')
    fecha2 = request.POST.get('fecha2')
  
    consulta4=Venta.objects.values('user').filter(fecha__range=[fecha1,fecha2]).annotate(total=Sum('valorTotal'))
    return render(request,'consultas/consulta4.html',{'consulta4':consulta4})
