from django.db import migrations, models

def agregar_usuarios_iniciales(apps, schema_editor):
    # Obtener el modelo Usuario (o credenciales si cambiaste el nombre)
    Usuario = apps.get_model('AppSolicitudes', 'Usuario')
    
    # Crear usuario administrador si no existe
    if not Usuario.objects.filter(nombre_usuario='admin').exists():
        Usuario.objects.create(nombre_usuario='admin', clave='admin')
    
    # Crear usuario estándar si no existe
    if not Usuario.objects.filter(nombre_usuario='usuario').exists():
        Usuario.objects.create(nombre_usuario='usuario', clave='usuario')

class Migration(migrations.Migration):

    dependencies = [
        ('AppSolicitudes', '0001_initial'),  # Asegúrate de que depende de la migración inicial
    ]

    operations = [
        migrations.RunPython(agregar_usuarios_iniciales),  # Ejecutar la función para agregar los usuarios
    ]
