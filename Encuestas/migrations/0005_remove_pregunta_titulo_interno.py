# Generated by Django 4.1.1 on 2023-04-13 14:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Encuestas', '0004_alter_pregunta_titulo_interno'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pregunta',
            name='titulo_interno',
        ),
    ]
