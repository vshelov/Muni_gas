# Generated by Django 5.0 on 2024-10-22 01:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppSolicitudes', '0003_alter_usuario_id_solicitud'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='solicitud',
            name='usuario',
        ),
        migrations.AlterField(
            model_name='solicitud',
            name='comuna',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='solicitud',
            name='direccion',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='solicitud',
            name='estado',
            field=models.CharField(choices=[('PENDIENTE', 'Pendiente'), ('ACEPTADA', 'Aceptada'), ('RECHAZADA', 'Rechazada'), ('EXPIRADA', 'Expirada')], default='PENDIENTE', max_length=10),
        ),
        migrations.AlterField(
            model_name='solicitud',
            name='rut',
            field=models.CharField(max_length=12),
        ),
        migrations.AlterField(
            model_name='solicitud',
            name='telefono',
            field=models.CharField(max_length=20),
        ),
    ]
