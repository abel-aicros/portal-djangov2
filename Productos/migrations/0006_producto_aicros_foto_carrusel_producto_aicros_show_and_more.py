# Generated by Django 4.1.1 on 2023-06-20 15:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Productos', '0005_alter_producto_aicros_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='producto_aicros',
            name='foto_carrusel',
            field=models.ImageField(blank=True, default='../static/img/AicrosIdentificador.png', upload_to='Página Productos/Aicros/Imágenes/Imágenes', verbose_name='Foto Carrusel'),
        ),
        migrations.AddField(
            model_name='producto_aicros',
            name='show',
            field=models.BooleanField(default=True, verbose_name='Mostrar en carrusel'),
        ),
        migrations.AddField(
            model_name='producto_aicros',
            name='show_image',
            field=models.BooleanField(default=True, verbose_name='Mostrar imagen'),
        ),
        migrations.AddField(
            model_name='producto_aicros',
            name='show_text',
            field=models.BooleanField(default=True, verbose_name='Mostrar texto'),
        ),
        migrations.AddField(
            model_name='producto_distribuido_aicros',
            name='foto_carrusel',
            field=models.ImageField(blank=True, default='../static/img/AicrosIdentificador.png', upload_to='Página Productos/Aicros/Distribuidos/Imágenes', verbose_name='Foto Carrusel'),
        ),
        migrations.AddField(
            model_name='producto_distribuido_aicros',
            name='show',
            field=models.BooleanField(default=True, verbose_name='Mostrar en carrusel'),
        ),
        migrations.AddField(
            model_name='producto_distribuido_aicros',
            name='show_image',
            field=models.BooleanField(default=True, verbose_name='Mostrar imagen'),
        ),
        migrations.AddField(
            model_name='producto_distribuido_aicros',
            name='show_text',
            field=models.BooleanField(default=True, verbose_name='Mostrar texto'),
        ),
        migrations.AlterField(
            model_name='producto_aicros',
            name='foto',
            field=models.ImageField(blank=True, default='../static/img/AicrosIdentificador.png', upload_to='Página Productos/Aicros/Imágenes/Imágenes', verbose_name='Foto Carrusel'),
        ),
    ]
