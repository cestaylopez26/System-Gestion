# Generated by Django 3.2.8 on 2022-04-30 15:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('libreria', '0002_rename_description_libro_descripcion'),
    ]

    operations = [
        migrations.AlterField(
            model_name='libro',
            name='descripcion',
            field=models.TextField(null=True, verbose_name='Descripción'),
        ),
    ]
