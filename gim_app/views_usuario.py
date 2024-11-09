# Create your views here.
from django.shortcuts import render
from django.shortcuts import render, redirect
from.forms import UsuarioForm
from django.contrib.auth import authenticate, login
from.models import AdminProfile
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib import messages
from django.shortcuts import get_object_or_404, render
import os
from django.db.models import Sum








@csrf_exempt
def eliminar_usuario(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        try:
            user = User.objects.get(username=username)
            user.delete()
            return HttpResponseRedirect(reverse('mostrar_usuarios'))  # Redirige a la página de usuarios
        except User.DoesNotExist:
            return HttpResponseRedirect(reverse('error'))  # Redirige a una página de error o maneja el caso de usuario no encontrado
    else:
        return HttpResponseRedirect(reverse('error'))  # Redirige a una página de error si la solicitud no es POST



def mostrar_usuarios(request):
    users = User.objects.all()  # Recupera todos los usuarios
    return render(request, 'mostrar_usuarios.html', {'users': users})





def registrar_admin(request):
    if request.method == 'POST':
        form = UsuarioForm(request.POST)
        if form.is_valid():
            # Verificar si el nombre de usuario ya existe
            username = form.cleaned_data['username']
            if User.objects.filter(username=username).exists():
                form.add_error('username', 'El nombre de usuario ya está en uso. Por favor, elige otro.')
                return render(request, 'registrar_usuario.html', {'form': form},)
            
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            
            # Asignar el perfil de administrador basado en el valor de 'is_admin'
            admin_profile, created = AdminProfile.objects.get_or_create(user=user)
            admin_profile.is_admin = form.cleaned_data['is_admin']
            
            # Procesar las nuevas opciones seleccionadas por el usuario
            
            admin_profile.save()
            
            # Aquí puedes agregar la lógica para enviar un correo de confirmación, etc.
            return render(request, 'registrar_usuario.html', {
                    'success': 'gurdado.', }) 
    else:
        form = UsuarioForm()
    return render(request, 'registrar_usuario.html', {'form': form})