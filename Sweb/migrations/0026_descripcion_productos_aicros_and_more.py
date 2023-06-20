# Generated by Django 4.1.1 on 2022-10-17 04:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Sweb', '0025_documentos_de_rápido_acceso'),
    ]

    operations = [
        migrations.CreateModel(
            name='Descripcion_Productos_Aicros',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('título', models.CharField(max_length=50)),
                ('texto_1', models.TextField()),
            ],
            options={
                'verbose_name': 'Descripción Productos Aicros',
                'verbose_name_plural': 'Descripción Productos Aicros',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='Descripcion_Productos_Distribuidos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('título', models.CharField(max_length=50)),
                ('texto_1', models.TextField()),
            ],
            options={
                'verbose_name': 'Descripción Productos Distribuidos',
                'verbose_name_plural': 'Descripción Productos Distribuidos',
                'ordering': ['id'],
            },
        ),
        migrations.AlterModelOptions(
            name='documentos_de_rápido_acceso',
            options={'ordering': ['nombre'], 'verbose_name': 'Documento Rápido Acceso', 'verbose_name_plural': 'Documento Rápido Acceso'},
        ),
    ]
