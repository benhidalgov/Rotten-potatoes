# Generated by Django 5.0.6 on 2024-06-27 06:01

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Registro', '0004_alter_pelicula_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pelicula',
            name='descripcion',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='pelicula',
            name='duracion',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='pelicula',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='pelicula',
            name='nombre',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='pelicula',
            name='portada',
            field=models.ImageField(upload_to='portadas/'),
        ),
        migrations.AlterField(
            model_name='pelicula',
            name='precio',
            field=models.PositiveIntegerField(default=0, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(999999)]),
        ),
    ]
