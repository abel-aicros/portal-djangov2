# Generated by Django 4.1.1 on 2022-10-15 21:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Sweb', '0022_encabezado_documentos'),
    ]

    operations = [
        migrations.RenameField(
            model_name='encabezado_documentos',
            old_name='texto1',
            new_name='texto_1',
        ),
        migrations.RenameField(
            model_name='encabezado_documentos',
            old_name='texto2',
            new_name='texto_2',
        ),
    ]
