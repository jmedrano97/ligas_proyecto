# Generated by Django 4.1.7 on 2023-04-08 00:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('miliga', '0003_equipo_escudo_equipo_foto'),
    ]

    operations = [
        migrations.RenameField(
            model_name='equipo',
            old_name='escudo',
            new_name='escudo_img',
        ),
        migrations.RenameField(
            model_name='equipo',
            old_name='foto',
            new_name='foto_img',
        ),
    ]