from django.urls import path
from . import views

urlpatterns = [
    path('',views.realizarCompra,name='compra'),
    path('<str:idCompra>/',views.compraExitosa,name="compra-exitosa")
]