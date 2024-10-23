from django.shortcuts import render, redirect
from django.contrib import messages

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

def login_view(request):
    template_view = "login.html"
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            return redirect('login')  # redirige al dashboard
        else:
            return render(request, 'login.html',{'error': 'Credenciales inválidas'})
        
    return render(request, template_name=template_view)

def register_view(request):
    template_view = "register.html"
    return render(request, template_name=template_view)

def recover_password_view(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        
        # Aquí debes agregar la lógica para enviar un correo de recuperación
        # Por ejemplo, podrías usar Django's password reset functionality.
        
        # Simulación de envío exitoso
        messages.success(request, 'Recovery email sent!')
        return redirect('login')  # Redirige a la página de inicio de sesión después de enviar el email

    template_view = "recover.html"  # Asegúrate de crear esta plantilla
    return render(request, template_name=template_view)


