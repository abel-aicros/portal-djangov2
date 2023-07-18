# Generated by Django 4.2.2 on 2023-07-06 14:01

import colorfield.fields
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Alianza',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(default='Alianza de Aicros', max_length=100)),
                ('foto', models.ImageField(blank=True, null=True, upload_to='Página Home/Alianzas/Ímagen')),
            ],
            options={
                'verbose_name': 'Alianza',
                'verbose_name_plural': 'Alianza',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='AllianceTitle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('texto', models.CharField(blank=True, max_length=100, null=True)),
            ],
            options={
                'verbose_name': 'Texto para título de Alianzas',
                'verbose_name_plural': 'Texto para título de Alianzas',
                'db_table': 'index_title_alliance',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='BannerTitle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('texto', models.CharField(blank=True, max_length=100, null=True)),
                ('texto_negrita', models.CharField(blank=True, max_length=100, null=True)),
            ],
            options={
                'verbose_name': 'Texto para título de Banner',
                'verbose_name_plural': 'Texto para título de Banner',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='BussinesLinesTitle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('texto', models.CharField(blank=True, max_length=100, null=True)),
            ],
            options={
                'verbose_name': 'Texto para título de Lineas de negocio',
                'verbose_name_plural': 'Texto para título de Lineas de negocio',
                'db_table': 'index_title_buss_lines',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='Carrusel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('texto', models.CharField(blank=True, max_length=100, null=True)),
                ('foto', models.ImageField(blank=True, null=True, upload_to='productosFotos')),
            ],
            options={
                'verbose_name': 'Ímagen_para_Carrusel_de_Promociones',
                'verbose_name_plural': 'Ímagen_para_Carrusel_de_Promociones',
                'db_table': 'Ímagen_para_Carrusel_de_Promociones',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='Cifra',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('título', models.CharField(max_length=200)),
                ('número', models.CharField(max_length=50)),
                ('color', colorfield.fields.ColorField(default='#991A14', image_field=None, max_length=18, samples=None)),
                ('font_color', colorfield.fields.ColorField(default='#FFFF', image_field=None, max_length=18, samples=None)),
            ],
            options={
                'verbose_name': 'Cifra',
                'verbose_name_plural': 'Cifra',
                'ordering': ['título'],
            },
        ),
        migrations.CreateModel(
            name='InicioProducto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('description', models.TextField()),
            ],
            options={
                'verbose_name': 'Caja Productos',
                'verbose_name_plural': 'Caja Productos',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='InicioServicio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('título', models.CharField(blank=True, max_length=50, null=True)),
                ('descripción', models.TextField(blank=True, null=True)),
            ],
            options={
                'verbose_name': 'Caja_de_Servicios',
                'verbose_name_plural': 'Caja_de_Servicios',
                'db_table': 'Caja_de_Servicios',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='Líneas_de_Negocio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ícono', models.ImageField(blank=True, null=True, upload_to='Página Home/Líneas de Negocio/Ícono')),
                ('descripción', models.TextField()),
            ],
            options={
                'verbose_name': 'Línea de Negocio',
                'verbose_name_plural': 'Línea de Negocio',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='NewsTitle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('texto', models.CharField(blank=True, max_length=100, null=True)),
            ],
            options={
                'verbose_name': 'Texto para título de Noticias',
                'verbose_name_plural': 'Texto para título de Noticias',
                'db_table': 'index_title_news',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='Noticia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('título', models.CharField(default='Nueva Noticia', max_length=150)),
                ('foto', models.ImageField(default='../static/img/AicrosIdentificador.png', upload_to='Página Home/Noticias/')),
                ('Introducción_de_Noticia', models.TextField(max_length=200)),
                ('Continuación_de_Noticia', models.TextField()),
                ('Fecha', models.DateField(default=django.utils.timezone.now)),
                ('show', models.BooleanField(default=True, verbose_name='Mostrar Noticia')),
            ],
            options={
                'verbose_name': 'Noticia',
                'verbose_name_plural': 'Noticia',
                'ordering': ['-Fecha'],
            },
        ),
        migrations.CreateModel(
            name='Page404',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('texto', models.CharField(default='Página no encontrada!', max_length=100)),
                ('foto', models.ImageField(blank=True, default='../static/img/logo/invertido.png', upload_to='Página Home/')),
            ],
            options={
                'verbose_name': 'página 404',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='PromotionsTitle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('texto', models.CharField(blank=True, max_length=100, null=True)),
            ],
            options={
                'verbose_name': 'Texto para título de Promociones',
                'verbose_name_plural': 'Texto para título de Promociones',
                'db_table': 'index_title_promotions',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='StatsTitle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('texto', models.CharField(blank=True, max_length=100, null=True)),
            ],
            options={
                'verbose_name': 'Texto para título de La empresa en cifras',
                'verbose_name_plural': 'Texto para título de La empresa en cifras',
                'db_table': 'index_title_stats',
                'ordering': ['id'],
            },
        ),
    ]