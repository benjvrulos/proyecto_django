from django.shortcuts import render
from django.http import HttpResponse
from .models import Compra,SubCompra
from userAuths.models import User
from apps.Tienda.models import Producto

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
        print("Producto:",producto.nombre)
        print("Stock inicial:" , producto.stock)
        print("Precio: ", precio)
        print("Cantidad: ",p['cantidad'])
        producto.stock -= cantidad
        producto.save()
        print("Stock final: " , producto.stock)
        print("Subtotal: ", subtotal)
        subcompra = SubCompra.objects.create(compra=compra,producto=producto,cantidad= cantidad,subtotal=subtotal)
        total += subtotal


    print("Total de la compra: ", total)
    compra.total = total
    compra.save()


    return HttpResponse("Compra Exitosa")
