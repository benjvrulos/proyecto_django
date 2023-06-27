from django.urls import path
from userAuths import views

urlpatterns = [
    path('login/',views.loginView,name='login'),
    path('logout/',views.logoutView,name='logout'),
]