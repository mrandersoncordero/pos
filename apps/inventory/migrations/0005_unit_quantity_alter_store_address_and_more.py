# Generated by Django 5.1.6 on 2025-02-07 17:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("inventory", "0004_product_description"),
    ]

    operations = [
        migrations.AddField(
            model_name="unit",
            name="quantity",
            field=models.PositiveBigIntegerField(default=1),
        ),
        migrations.AlterField(
            model_name="store",
            name="address",
            field=models.TextField(blank=True, null=True, verbose_name="Direccion"),
        ),
        migrations.AlterField(
            model_name="unit",
            name="description",
            field=models.TextField(blank=True, null=True, verbose_name="Descripcion"),
        ),
    ]
