# Django
from django.db import models

# Models
from inventory.models import Product

# Utilities
from config.utils import MainModel


class Provider(MainModel, models.Model):
    name = models.CharField(max_length=200, verbose_name="Nombre")
    email = models.EmailField(unique=True, verbose_name="Correo")
    phone = models.CharField(max_length=20, verbose_name="Telefono")
    address = models.TextField(verbose_name="Direccion")

    class Meta:
        verbose_name = "Proveedor"
        verbose_name_plural = "Proveedores"

    def __str__(self):
        return self.name


class Purchase(MainModel, models.Model):
    provider = models.ForeignKey(
        Provider, on_delete=models.CASCADE, verbose_name="Proveedor"
    )
    total = models.DecimalField(
        max_digits=10, decimal_places=2, default=0, verbose_name="Total"
    )

    class Meta:
        verbose_name = "Compra"
        verbose_name_plural = "Compras"

    def __str__(self):
        return f"Compra {self.id} - {self.proveedor}"


class PurchaseDetail(models.Model):
    purchase = models.ForeignKey(
        Purchase, on_delete=models.CASCADE, verbose_name="Compra"
    )
    product = models.ForeignKey(
        Product, on_delete=models.CASCADE, verbose_name="Producto"
    )
    quantity = models.PositiveIntegerField(verbose_name="Cantidad", default=1)
    unit_price = models.DecimalField(
        max_digits=10, decimal_places=2, verbose_name="Precio Unitario"
    )

    class Meta:
        verbose_name = "Detalle de la compra"
        verbose_name_plural = "Detalles de las compras"

    def subtotal(self):
        return self.cantidad * self.precio_unitario

    def __str__(self):
        return f"{self.cantidad} x {self.producto.nombre}"
