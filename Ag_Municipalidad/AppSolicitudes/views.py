from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Solicitud
from django.utils import timezone
from datetime import timedelta


# Vistas para los templates de administrador y usuario
def administrador_dashboard(request):
    return render(request, 'administrador.html')

def inicio(request):
    return render(request, 'inicio.html')

def crear_solicitud(request):
    if request.method == 'POST':
        rut = request.POST.get('rut')
        nombre = request.POST.get('nombre')
        apellidos = request.POST.get('apellidos')
        direccion = request.POST.get('direccion')
        telefono = request.POST.get('telefono')
        comuna = request.POST.get('comuna')
        nueva_solicitud = Solicitud(rut=rut, nombre=nombre, apellidos=apellidos, direccion=direccion, telefono=telefono, comuna=comuna)
        nueva_solicitud.save()
        return render(request, 'MensajeExitoso.html')
    return render(request, 'TemplateAdministrador/ingresarSolicitud.html')


def eliminar_solicitud(request, id):
    solicitud = get_object_or_404(Solicitud, id=id)
    
    if request.method == 'POST':
        solicitud.delete()
        # Redirige de vuelta a la página de listado con un mensaje de éxito
        return render(request, 'TemplateAdministrador/EliminacionConfirm.html')
    
    # Muestra la confirmación de eliminación
    return render(request, 'TemplateAdministrador/BorrarSolicitud.html', {'solicitud': solicitud})

def buscar_solicitud(request):
    rut = request.GET.get('rut', None)
    
    if rut:
        solicitudes = Solicitud.objects.filter(rut=rut)  # Usamos filter() para obtener todas las solicitudes con ese RUT
        if solicitudes.exists():  # Verificamos si existen solicitudes
            return render(request, 'TemplateAdministrador/BuscarSolicitud.html', {'solicitudes': solicitudes})
        else:
            # Si no hay resultados, devolvemos un mensaje informando que no se encontró ninguna solicitud
            return render(request, 'TemplateAdministrador/BuscarSolicitud.html', {'error': 'No se encontró ninguna solicitud con ese RUT'})
    return render(request, 'TemplateAdministrador/BuscarSolicitud.html')

def editar_estado_solicitud(request, id):
    solicitud = get_object_or_404(Solicitud, id=id)

    if request.method == 'POST':
        nuevo_estado = request.POST.get('estado').lower()  # Convertir el valor del estado a minúsculas
        solicitud.estado = nuevo_estado
        
        # Si el estado es "aceptada", actualizamos la fecha de aceptación
        if nuevo_estado == 'aceptada':
            solicitud.fecha_aceptacion = timezone.now()  # Usamos timezone.now() sin astimezone()
        else:
            solicitud.fecha_aceptacion = None

        solicitud.save()
        return redirect('listar')

    return render(request, 'TemplateAdministrador/EditarSolicitud.html', {'solicitud': solicitud})

def ListarSolicitud(request):
    rut_query = request.GET.get('rut', None)  # Capturamos el parámetro 'rut' desde el request
    solicitudes = Solicitud.objects.all()  # Obtener todas las solicitudes

    # Verificar si las solicitudes han expirado
    for solicitud in solicitudes:
        # Si la solicitud no está expirada y ha pasado un mes desde la fecha de solicitud
        if solicitud.estado != 'expirada' and timezone.now() > solicitud.fecha_solicitud + timedelta(days=30):
            solicitud.estado = 'expirada'
            solicitud.save()

    # Si hay una búsqueda, filtrar por RUT
    if rut_query:
        solicitudes = Solicitud.objects.filter(rut__icontains=rut_query)
        return render(request, 'TemplateAdministrador/ListarSolicitud.html', {
            'solicitudes': solicitudes,  # Mostramos los resultados de la búsqueda
            'rut_query': rut_query  # Para mantener el valor del RUT en el input de búsqueda
        })

    # Filtrar las solicitudes según su estado si no hay búsqueda
    solicitudes_pendientes = Solicitud.objects.filter(estado='pendiente')
    solicitudes_aceptadas = Solicitud.objects.filter(estado='aceptada')
    solicitudes_rechazadas = Solicitud.objects.filter(estado='rechazada')
    solicitudes_expiradas = Solicitud.objects.filter(estado='expirada')

    return render(request, 'TemplateAdministrador/ListarSolicitud.html', {
        'solicitudes_pendientes': solicitudes_pendientes,
        'solicitudes_aceptadas': solicitudes_aceptadas,
        'solicitudes_rechazadas': solicitudes_rechazadas,
        'solicitudes_expiradas': solicitudes_expiradas,
        'rut_query': rut_query  # Para mantener el RUT en el input de búsqueda
    })

def detalles_solicitud(request, id):
    solicitud = get_object_or_404(Solicitud, id=id)
    return render(request, 'TemplateAdministrador/DetalleSolicitud.html', {'solicitud': solicitud})
