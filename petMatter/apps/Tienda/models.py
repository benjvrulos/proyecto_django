from django.db import models

# Create your models here.
class Categoria(models.Model):
    id_categoria = models.IntegerField(primary_key=True)
    nombre_categoria = models.CharField(max_length=100)

    def __str__(self):
        return 'Nombre: {} - ID: {}'.format(self.id_categoria,self.nombre_categoria)
    
class Producto(models.Model):
    sku = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=50)
    stock = models.IntegerField()
    precio = models.IntegerField()
    descripcion = models.CharField(max_length=250)
    id_categoria = models.ForeignKey(Categoria,on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to='imagenesProducto')

    def __str__(self):
        return 'N°: {} - Stock: {} - Nombre: {}'.format(self.sku,self.stock,self.nombre)
    
