from django.shortcuts import render
from django.http import HttpResponse
from .models import Compra
from userAuths.models import User
import json

def realizarCompra(request):
    productos = json.loads(request.body)
    for p in productos:
        print("TITULO: ",p['titulo'])
        print("CANTIDAD: ",p['cantidad'])

    return HttpResponse("Compra Exitosa")
