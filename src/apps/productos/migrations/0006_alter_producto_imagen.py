# Generated by Django 4.0.5 on 2022-07-12 14:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('productos', '0005_rename_categoria_marca_producto_categoria_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='imagen',
            field=models.ImageField(blank=True, null=True, upload_to='productos'),
        ),
    ]
