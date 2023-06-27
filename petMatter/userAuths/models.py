from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    email = models.EmailField(unique=True)
    username = models.CharField(unique=True,max_length=200)
    rut = models.CharField(unique=True,max_length=20)
    nombres = models.CharField(max_length=200)
    apellidos = models.CharField(max_length=200)
    fechaNacimiento = models.DateField()
    is_superuser = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['rut','username','nombres','apellidos']

    def __str__(self):
        return self.username