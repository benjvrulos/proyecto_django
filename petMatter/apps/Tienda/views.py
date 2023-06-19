from django.shortcuts import render,reverse,redirect
from .models import Producto,Categoria

def index(request):
    return render(request,'Tienda/index.html')

def mantenedor(request):
    categorias = Categoria.objects.all()
    productos = Producto.objects.all()
    return render(request,'Tienda/mantenedor.html',{'productos':productos,'categorias':categorias})

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
