from django.shortcuts import render,redirect,reverse
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from userAuths.models import User
def registerView(request):

    if request.method == 'POST':
        email = request.POST['emailUsuario']
        username = request.POST['usernameUsuario']
        rut = request.POST['rutUsuario']
        nombres = request.POST['nombreUsuario']
        apellidos = request.POST['apellidosUsuario']
        fecha = request.POST['fechaNacimientoUsuario']
        password = request.POST['passwordUsuario']

        User.objects.create_user(email=email,username=username,rut=rut,nombres=nombres,apellidos=apellidos,
                         fechaNacimiento=fecha,password=password)
        user = authenticate(request,username=username,password= password)
        if user is not None:
            return redirect(reverse("home"))

        else:
            messages.warning(request,"Usuario o contraseña inválidos")

    elif request.user.is_authenticated:
        # messages.warning(request,f"Ya estás registrado 😊")
        return redirect('home')

    else:
        pass

    return render(request,'userAuths/register.html')

def loginView(request):
    if request.method == 'POST':
        username = request.POST['usernameUsuario']
        password = request.POST['passwordUsuario']
        user = authenticate(request,username=username,password=password)
        if user is not None: #if there is a user
            login(request,user)
            messages.success(request,"Has ingresado exitosamente.")
            return redirect("home")
        else:
            messages.error(request,"Usuario o contraseña incorrecta")
            return redirect("login")

    return render(request,'userAuths/login.html')

def logoutView(request):
    logout(request)
    messages.success(request,"Te has salido exitosamente.")
    return redirect(reverse('home'))