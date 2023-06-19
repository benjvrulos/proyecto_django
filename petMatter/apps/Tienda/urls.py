from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='home'),
    path('mantenedor/', views.mantenedor,name='mantenedor'),
    path('agregarProducto/',views.agregarProducto,name='agregar-producto')
]