# Generated by Django 5.1 on 2024-10-18 18:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tareas', '0002_auto_20241018_1323'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tarea',
            name='nombre',
            field=models.CharField(max_length=200),
        ),
    ]
