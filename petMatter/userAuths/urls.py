from django.urls import path
from userAuths import views

urlpatterns = [
    path('login/',views.LoginView,name='login'),
]