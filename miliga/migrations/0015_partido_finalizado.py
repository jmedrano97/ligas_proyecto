# Generated by Django 4.1.7 on 2023-04-27 02:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('miliga', '0014_alter_jornada_fecha_inicio_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='partido',
            name='finalizado',
            field=models.BooleanField(default=False),
        ),
    ]
