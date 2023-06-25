from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='home'),
    path('mantenedor/', views.mantenedor,name='mantenedor'),
    path('agregarProducto/',views.agregarProducto,name='agregar-producto'),
    path('editarProducto/',views.editarProducto,name='editar-producto'),
    path('eliminarProducto/<int:sku>/',views.eliminarProducto,name='eliminar-producto'),
    path('editarProductoAjax/',views.ajax_post_view,name='editar-producto-ajax'),

]