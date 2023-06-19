from django.shortcuts import render
from .models import Producto

def index(request):
    return render(request,'Tienda/index.html')

def mantenedor(request):
    productos = Producto.objects.all()
    return render(request,'Tienda/mantenedor.html',{'productos':productos})