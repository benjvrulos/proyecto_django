from django.shortcuts import render,reverse,redirect
from .models import Producto,Categoria
import os
from django.conf import settings
from django.http import JsonResponse
from django.core import serializers
from django.http import HttpResponseNotAllowed
import json
from django.contrib.auth.decorators import login_required, permission_required,user_passes_test

def index(request):
    return render(request,'Tienda/index-2.html')

@user_passes_test(lambda u: u.is_superuser)
def mantenedor(request):
    categorias = Categoria.objects.all()
    productos = Producto.objects.all()
    return render(request,'Tienda/mantenedor.html',{'productos':productos,'categorias':categorias})

def productoView(request):
    productos = Producto.objects.all()
    productos = Producto.objects.filter(stock__gt=0)

    return render(request,'Tienda/producto.html',{'productos':productos})

def agregarProducto(request):
    v_sku = request.POST['skuProducto']
    v_nombre = request.POST['nombreProducto']
    v_stock = request.POST['stockProducto']
    v_precio = request.POST['precioProducto']
    v_descripcion = request.POST['descripicionProducto']
    v_img = request.FILES['imagenProducto']
    v_categoria = Categoria.objects.get(id_categoria = request.POST['cmbCategoria'])

    Producto.objects.create(sku = v_sku,nombre = v_nombre,stock = v_stock,precio = v_precio,descripcion = v_descripcion, id_categoria = v_categoria, imagen = v_img)        

    return redirect('mantenedor')


def editarProducto(request):
    v_sku = request.POST['skuProductoEditar']
    producto = Producto.objects.get(sku=v_sku)
    v_nombre = request.POST['nombreProductoEditar']
    v_stock = request.POST['stockProductoEditar']
    v_precio = request.POST['precioProductoEditar']
    v_descripcion = request.POST['descripcionProductoEditar']
    v_categoria = Categoria.objects.get(id_categoria = request.POST['cmbCategoriaEditar'])

    try:
        v_img = request.FILES['imagenProductoEditar']
        ruta_imagen = os.path.join(settings.MEDIA_ROOT, str(producto.imagen))
        os.remove(ruta_imagen)
    except:
        v_img = producto.imagen
    
    producto.nombre = v_nombre
    producto.stock = v_stock
    producto.precio = v_precio
    producto.descripcion = v_descripcion
    producto.imagen = v_img
    producto.id_categoria = v_categoria

    producto.save()
    return redirect('mantenedor')


def eliminarProducto(request,sku):
    producto = Producto.objects.get(sku = sku)
    ruta_imagen = os.path.join(settings.MEDIA_ROOT, str(producto.imagen))
    os.remove(ruta_imagen)
    producto.delete()
    return redirect('mantenedor')

def ajax_post_view(request):
    sku = json.load(request)['skuProducto']
    data = list(Producto.objects.filter(sku=sku).values())
    return JsonResponse(data,safe=False)
