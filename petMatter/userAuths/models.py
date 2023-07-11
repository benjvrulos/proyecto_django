from django.db import models
from django.contrib.auth.models import AbstractUser
from userAuths.managers import CustomUserManager

class User(AbstractUser):
    email = models.EmailField(unique=True)
    username = models.CharField(unique=True,max_length=200)
    rut = models.CharField(unique=True,max_length=20)
    nombres = models.CharField(max_length=200)
    apellidos = models.CharField(max_length=200)
    fechaNacimiento = models.DateField()
    is_superuser = models.BooleanField(default=False)

    REQUIRED_FIELDS = ['rut','email','nombres','apellidos','fechaNacimiento']
    # objects = CustomUserManager()

    def __str__(self):
        return self.username