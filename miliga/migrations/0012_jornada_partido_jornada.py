# Generated by Django 4.1.7 on 2023-04-26 22:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('miliga', '0011_alter_partido_hora_inicio_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Jornada',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numero', models.IntegerField()),
                ('fecha_inicio', models.DateField()),
                ('fecha_terminacion', models.DateField()),
            ],
        ),
        migrations.AddField(
            model_name='partido',
            name='jornada',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='miliga.jornada'),
        ),
    ]