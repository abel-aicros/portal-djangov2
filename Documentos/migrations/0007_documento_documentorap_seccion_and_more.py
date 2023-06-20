# Generated by Django 4.1.1 on 2023-06-19 18:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Documentos', '0006_alter_cendadocumentstitle_texto_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Documento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=500)),
                ('doc_file', models.FileField(default='Página Documentos/Documentos/default.docx', upload_to='Página Documentos/Documentos', verbose_name='Archivo')),
            ],
            options={
                'verbose_name': 'Document',
                'db_table': 'document',
                'ordering': ['nombre'],
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='DocumentoRap',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=500)),
                ('doc_file', models.FileField(default='Página Documentos/Documentos/default.docx', upload_to='Página Documentos/Documentos', verbose_name='Archivos')),
            ],
            options={
                'verbose_name': 'Documento rápido',
                'verbose_name_plural': 'Documentos rápidos',
                'ordering': ['nombre'],
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Seccion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('texto', models.CharField(blank=True, default='Sección de Documentos', max_length=100)),
            ],
            options={
                'verbose_name': 'Seccion de documentos',
                'verbose_name_plural': 'Secciones de documentos',
                'db_table': 'section',
                'ordering': ['id'],
                'managed': True,
            },
        ),
        migrations.DeleteModel(
            name='CendaDocumentsTitle',
        ),
        migrations.DeleteModel(
            name='Contrato_Específico_Columna_1',
        ),
        migrations.DeleteModel(
            name='Contrato_Específico_Columna_2',
        ),
        migrations.DeleteModel(
            name='Contrato_Específico_Columna_3',
        ),
        migrations.DeleteModel(
            name='Contrato_General_Columna_1',
        ),
        migrations.DeleteModel(
            name='Contrato_General_Columna_2',
        ),
        migrations.DeleteModel(
            name='Contrato_General_Columna_3',
        ),
        migrations.DeleteModel(
            name='Documentos_de_Rápido_Acceso',
        ),
        migrations.DeleteModel(
            name='GeneralContractTitle',
        ),
        migrations.DeleteModel(
            name='Listado_Productos_y_Servicios_Columna_1',
        ),
        migrations.DeleteModel(
            name='Listado_Productos_y_Servicios_Columna_2',
        ),
        migrations.DeleteModel(
            name='Listado_Productos_y_Servicios_Columna_3',
        ),
        migrations.DeleteModel(
            name='MiconsDocumentsTitle',
        ),
        migrations.DeleteModel(
            name='OtherDocumentsTitle',
        ),
        migrations.DeleteModel(
            name='Otros_Documentos_Columna_1',
        ),
        migrations.DeleteModel(
            name='Otros_Documentos_Columna_2',
        ),
        migrations.DeleteModel(
            name='Otros_Documentos_Columna_3',
        ),
        migrations.DeleteModel(
            name='Registro_y_Certificaciones_de_Software_CENDA_Columna_1',
        ),
        migrations.DeleteModel(
            name='Registro_y_Certificaciones_de_Software_CENDA_Columna_2',
        ),
        migrations.DeleteModel(
            name='Registro_y_Certificaciones_de_Software_CENDA_Columna_3',
        ),
        migrations.DeleteModel(
            name='Registro_y_Certificaciones_de_Software_MICONS_Columna_1',
        ),
        migrations.DeleteModel(
            name='Registro_y_Certificaciones_de_Software_MICONS_Columna_2',
        ),
        migrations.DeleteModel(
            name='Registro_y_Certificaciones_de_Software_MICONS_Columna_3',
        ),
        migrations.DeleteModel(
            name='ServicesProductsListTitle',
        ),
        migrations.DeleteModel(
            name='SpecificContractTitle',
        ),
        migrations.AddField(
            model_name='documento',
            name='seccion',
            field=models.ManyToManyField(to='Documentos.seccion', verbose_name='sección'),
        ),
    ]
