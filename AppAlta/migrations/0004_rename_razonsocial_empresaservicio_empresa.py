# Generated by Django 4.1.3 on 2023-01-30 20:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('AppAlta', '0003_empresaservicio_imagenequipo'),
    ]

    operations = [
        migrations.RenameField(
            model_name='empresaservicio',
            old_name='razonSocial',
            new_name='empresa',
        ),
    ]