# Generated by Django 4.1.1 on 2022-10-17 21:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Sweb', '0026_descripcion_productos_aicros_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Descripcion_Servicios_Aicros',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('título', models.CharField(max_length=50)),
                ('texto_1', models.TextField()),
            ],
            options={
                'verbose_name': 'Descripcion Servicio Aicros',
                'verbose_name_plural': 'Descripcion Servicio Aicros',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='Encabezado_Servicio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('título', models.CharField(max_length=50)),
                ('texto_1', models.TextField()),
                ('texto_2', models.TextField()),
            ],
            options={
                'verbose_name': 'Encabezado Servicio',
                'verbose_name_plural': 'Encabezado Servicio',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='Servicio_Aicros',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ícono', models.ImageField(upload_to='Página Servicios/Ícono')),
                ('descripción', models.TextField()),
            ],
            options={
                'verbose_name': 'Producto Aicros',
                'verbose_name_plural': 'Producto Aicros',
                'ordering': ['id'],
            },
        ),
    ]
