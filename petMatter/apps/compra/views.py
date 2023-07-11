from django.shortcuts import render,redirect
from django.urls import reverse,reverse_lazy
from .models import Compra,SubCompra,UUIDEncoder
from apps.Tienda.models import Producto
from django.http import JsonResponse
from django.contrib import messages

import json

def realizarCompra(request):
    productos = json.loads(request.body)

    total = 0
    compra = Compra.objects.create(user=request.user,total=total)
    for p in productos:
        producto = Producto.objects.get(sku=p['sku'])
        precio = producto.precio
        cantidad = p['cantidad']
        subtotal = precio * cantidad
        producto.stock -= cantidad

        if(producto.stock < 0):
            messages.error(request,f"Su compra supera el stock disponible") 
            return redirect('home')
        
        producto.save()
        subcompra = SubCompra.objects.create(compra=compra,producto=producto,cantidad= cantidad,subtotal=subtotal)
        total += subtotal


    compra.total = total
    compra.save()
    data = []
    data.append({'idCompra':str(compra.idCompra)})
    print(data)
    return JsonResponse(data,safe=False)

def compraExitosa(request, idCompra):
    compra = Compra.objects.get(idCompra=idCompra)
    print(compra)
    return render(request,'compra/compra.html',{'compra':compra})
