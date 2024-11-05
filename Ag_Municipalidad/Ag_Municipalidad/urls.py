from django.contrib import admin
from django.urls import path
from AppSolicitudes.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', inicio, name='inicio'),
    path('administrador/', administrador_dashboard, name='administrador_dashboard'), 
    path('ingresar/', crear_solicitud, name='solicitud'),
    path('eliminar/<int:id>/', eliminar_solicitud, name='eliminar_solicitud'),
    path('buscar/', buscar_solicitud, name='buscar_solicitud'),
    path('editar_estado/<int:id>/', editar_estado_solicitud, name='editar_estado_solicitud'),
    path('listar/', ListarSolicitud, name='listar'),
    path('solicitudes/detalles/<int:id>/', detalles_solicitud, name='detalles_solicitud'),
]
