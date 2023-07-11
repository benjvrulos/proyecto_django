import uuid
from django.db import models
from apps.Tienda.models import Producto
from userAuths.models import User

class Compra(models.Model):
    idCompra = models.UUIDField(primary_key=True,unique=True,default=uuid.uuid4,editable=False)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    productos = models.ManyToManyField(Producto,through='SubCompra')
    total = models.IntegerField()

    def __str__(self):
        return f"ID COMPRA: {self.idCompra}  USUARIO RUT:{self.user.rut} TOTAL:{self.total}" 

class SubCompra(models.Model):
    compra = models.ForeignKey(Compra,on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto,on_delete=models.CASCADE)
    cantidad = models.IntegerField()
    subtotal = models.IntegerField()

    def __str__(self):
        return f"ID COMPRA: {self.compra.idCompra}  ID PRODUCTO: {self.producto.sku}  CANTIDAD: {self.cantidad} SUBTOTAL: {self.subtotal}" 


    
