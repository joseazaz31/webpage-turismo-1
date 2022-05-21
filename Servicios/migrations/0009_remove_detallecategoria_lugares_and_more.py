# Generated by Django 4.0.3 on 2022-05-19 23:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Places', '0001_initial'),
        ('Servicios', '0008_remove_detallecategoria_planes'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='detallecategoria',
            name='lugares',
        ),
        migrations.AddField(
            model_name='detallecategoria',
            name='lugares',
            field=models.ManyToManyField(to='Places.lugares'),
        ),
    ]
