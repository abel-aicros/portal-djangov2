# Generated by Django 4.1.1 on 2023-03-29 14:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Sweb', '0049_alter_carrusel_options_alter_inicioservicio_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='noticia_1',
            name='Introducción_de_Noticia',
            field=models.TextField(max_length=150),
        ),
        migrations.AlterField(
            model_name='noticia_2',
            name='Introducción_de_Noticia',
            field=models.TextField(max_length=150),
        ),
        migrations.AlterField(
            model_name='noticia_3',
            name='Introducción_de_Noticia',
            field=models.TextField(max_length=150),
        ),
    ]
