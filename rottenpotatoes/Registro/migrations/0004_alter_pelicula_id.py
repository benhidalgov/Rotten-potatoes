# Generated by Django 5.0.6 on 2024-06-27 02:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Registro', '0003_alter_pelicula_nombre'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pelicula',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
