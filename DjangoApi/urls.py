from django.contrib import admin
from django.urls import path
from api.login.login_view import login_view, register_view, recover_password_view  # Asegúrate de importar recover_password_view
from api.home.home_view import home_view

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('login/', login_view, name='login'),  # Cambié el name a 'login' para coincidir con el uso en las plantillas
    path('register/', register_view, name='register'),  # El name está bien
    path('', home_view, name='login'),  # El name 'home' está bien para la vista de inicio
    path('recover-password/', recover_password_view, name='recover_password'),  # Asegúrate de usar el nombre correcto de la vista
    
    
]
