# Generated by Django 4.2.6 on 2023-11-01 04:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inicio', '0002_rename_anios_paleta_anio_paleta_mod'),
    ]

    operations = [
        migrations.RenameField(
            model_name='paleta',
            old_name='mod',
            new_name='modelo',
        ),
    ]