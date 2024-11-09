from django.shortcuts import render, redirect
from django.contrib.auth import authenticate
from.models import AdminProfile






def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        if username == "killua" and password == "1":
            return redirect('admin')  # Redirige al usuario a la página de administrador si son los valores específicos
        user = authenticate(request, username=username, password=password)
        if user is not None:
            # Verificar si el usuario es administrador
            admin_profile = AdminProfile.objects.get(user=user)
            if admin_profile.is_admin:
                return redirect('admin')  # Redirige al usuario a la página de administrador si es administrador
            else:
                return redirect('inicio')  # Redirige al usuario a la página de inicio si no seleccionó ninguna de las opciones
        else:
            error_message = "Nombre de usuario o contraseña incorrectos."
            return render(request, 'login.html', {'error_message': error_message})
    else:
        return render(request, 'login.html')



def admin(request):
    return render(request,'admin.html')