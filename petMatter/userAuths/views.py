from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from userAuths.models import User
def RegisterView(request):

    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        user = authenticate(request,username=email,password= password)
        login(request,user)
        if user is not None:
            login(request=user)
            return redirect("apps.Tienda:index")

        else:
            messages.warning(request,"Usuario o contraseña inválidos")

    elif request.user.is_authenticated:
        messages.warning(request,f"Ya estás registrado 😊")
        return redirect('apps.Tienda:index')

    else:
        pass

    return render(request,'userAuths/register.html')

def LoginView(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']

        user = User.objects.get(email= email)
        user = authenticate(request,email=email,password=password)
        if user is not None: #if there is a user
                login(request,user)
                messages.success(request,"You are logged.")
                return redirect("core:index")
        else:
                messages.warning(request,"Usuario o contraseña incorrecta")
                return redirect("userauths:sign-in")

    return render(request,'userAuths/login.html')