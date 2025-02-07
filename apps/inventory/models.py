"""Inventory models."""

# Django
from django.db import models

# Utilities
from config.utils import MainModel


class Category(MainModel, models.Model):
    name = models.CharField(max_length=100, unique=True, verbose_name="Nombre")
    description = models.TextField(verbose_name="Descripcion", null=True, blank=True)

    class Meta:
        verbose_name = "Categoria"  # Nombre en singular en Django Admin
        verbose_name_plural = "Categorias"  # Nombre en plural en Django Admin

    def __str__(self):
        return self.name


class Unit(MainModel, models.Model):
    name = models.CharField(max_length=50, unique=True, verbose_name="Nombre")
    description = models.TextField(verbose_name="Descripcion", null=True, blank=True)
    quantity = models.PositiveBigIntegerField(default=1)

    class Meta:
        verbose_name = "Unidad"  # Nombre en singular en Django Admin
        verbose_name_plural = "Unidades"  # Nombre en plural en Django Admin
        indexes = [
            models.Index(fields=["active"]),
        ]

    def __str__(self):
        return self.name


class Store(MainModel, models.Model):
    name = models.CharField(max_length=50, unique=True, verbose_name="Nombre")
    address = models.TextField(verbose_name="Direccion", null=True, blank=True)

    class Meta:
        verbose_name = "Almacen"  # Nombre en singular en Django Admin
        verbose_name_plural = "Almacenes"  # Nombre en plural en Django Admin

    def __str__(self):
        return self.name


class Product(MainModel, models.Model):
    name = models.CharField(max_length=200, verbose_name="Nombre", unique=True)
    description = models.TextField(verbose_name="Descripcion", null=True, blank=True)
    category = models.ForeignKey(
        Category,
        related_name="products",
        on_delete=models.CASCADE,
        verbose_name="Categoria",
    )
    unit = models.ForeignKey(
        Unit, related_name="units", on_delete=models.CASCADE, verbose_name="Unidad"
    )
    store = models.ForeignKey(
        Store, related_name="stores", on_delete=models.CASCADE, verbose_name="Almacen"
    )
    stock = models.PositiveIntegerField(default=0, verbose_name="Cantidad en Stock")
    purchase_price = models.DecimalField(
        max_digits=10, decimal_places=2, verbose_name="Precio de compra"
    )
    price_sale = models.DecimalField(
        max_digits=10, decimal_places=2, verbose_name="Precio de venta"
    )

    class Meta:
        verbose_name = "Producto"  # Nombre en singular en Django Admin
        verbose_name_plural = "Productos"  # Nombre en plural en Django Admin
        ordering = ["name"]
        indexes = [
            models.Index(fields=["id"]),
            models.Index(fields=["name"]),
            models.Index(fields=["-created"]),
        ]

    def __str__(self):
        return f"{self.name} ({self.stock})"
