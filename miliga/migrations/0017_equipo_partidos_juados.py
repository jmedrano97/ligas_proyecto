# Generated by Django 4.1.7 on 2023-04-28 02:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('miliga', '0016_jornada_vuelta'),
    ]

    operations = [
        migrations.AddField(
            model_name='equipo',
            name='partidos_juados',
            field=models.IntegerField(default=0),
        ),
    ]