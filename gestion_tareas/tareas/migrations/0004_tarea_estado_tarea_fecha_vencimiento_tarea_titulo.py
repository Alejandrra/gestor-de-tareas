# Generated by Django 5.1 on 2024-10-24 23:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tareas', '0003_alter_tarea_nombre'),
    ]

    operations = [
        migrations.AddField(
            model_name='tarea',
            name='estado',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='tarea',
            name='fecha_vencimiento',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='tarea',
            name='titulo',
            field=models.CharField(default='Nueva Tarea', max_length=200),
        ),
    ]
