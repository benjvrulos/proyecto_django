
from django.urls import path
from . import views

urlpatterns = [
    path('',views.todosProductosJson.as_view(),name='todos-productos-json'),
]