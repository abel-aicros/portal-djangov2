# Generated by Django 4.1.1 on 2022-10-14 02:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Sweb', '0019_registro_y_certificaciones_de_software_columna_1_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contrato_General_Columna_1',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=500)),
                ('documento', models.FileField(blank=True, null=True, upload_to='Página Documentos/Contratos Generales/Documentos/Columna 1')),
                ('ícono', models.ImageField(blank=True, null=True, upload_to='Página Documentos/Contratos Generales/Íconos/Columna 1')),
            ],
            options={
                'verbose_name': 'Contrato General Columna 1',
                'verbose_name_plural': 'Contrato General Columna 1',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='Contrato_General_Columna_2',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=500)),
                ('documento', models.FileField(blank=True, null=True, upload_to='Página Documentos/Contratos Generales/Documentos/Columna 2')),
                ('ícono', models.ImageField(blank=True, null=True, upload_to='Página Documentos/Contratos Generales/Íconos/Columna 2')),
            ],
            options={
                'verbose_name': 'Contrato General Columna 2',
                'verbose_name_plural': 'Contrato General Columna 2',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='Contrato_General_Columna_3',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=500)),
                ('documento', models.FileField(blank=True, null=True, upload_to='Página Documentos/Contratos Generales/Documentos/Columna 3')),
                ('ícono', models.ImageField(blank=True, null=True, upload_to='Página Documentos/Contratos Generales/Íconos/Columna 3')),
            ],
            options={
                'verbose_name': 'Contrato General Columna 3',
                'verbose_name_plural': 'Contrato General Columna 3',
                'ordering': ['id'],
            },
        ),
        migrations.DeleteModel(
            name='Contrato_Columna1',
        ),
        migrations.DeleteModel(
            name='Contrato_Columna2',
        ),
        migrations.DeleteModel(
            name='Contrato_Columna3',
        ),
    ]
