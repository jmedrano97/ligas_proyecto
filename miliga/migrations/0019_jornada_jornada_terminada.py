# Generated by Django 4.1.7 on 2023-04-28 09:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('miliga', '0018_partido_resultado_confirmado'),
    ]

    operations = [
        migrations.AddField(
            model_name='jornada',
            name='jornada_terminada',
            field=models.BooleanField(default=False),
        ),
    ]
