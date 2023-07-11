import uuid
from django.db import models
from apps.Tienda.models import Producto
from userAuths.models import User
from rest_framework import serializers
import json
from uuid import UUID

class Compra(models.Model):
    idCompra = models.UUIDField(primary_key=True,unique=True,default=uuid.uuid4,editable=False)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    productos = models.ManyToManyField(Producto,through='SubCompra')
    total = models.IntegerField(default=0)

    def __str__(self):
        return str(self.idCompra) 
    
class CompraSerializer(serializers.ModelSerializer):
    class Meta:
        model = Compra
        fields = ['idCompra']
    
class SubCompra(models.Model):
    compra = models.ForeignKey(Compra,on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto,on_delete=models.CASCADE)
    cantidad = models.IntegerField()
    subtotal = models.IntegerField()

    def __str__(self):
        return f"ID COMPRA: {self.compra.idCompra}  ID PRODUCTO: {self.producto.sku}  CANTIDAD: {self.cantidad} SUBTOTAL: {self.subtotal}" 

class UUIDEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj,UUID):
            return obj.hex
        return json.JSONEncoder.default(self,obj)

    
