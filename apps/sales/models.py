# Django
from django.db import models

# Models
from inventory.models import Product

# Utilities
from config.utils import MainModel


class Client(MainModel, models.Model):
    name = models.CharField(max_length=200, verbose_name="Nombre")
    email = models.EmailField(unique=True, verbose_name="Correo")
    phone = models.CharField(max_length=20, verbose_name="Telefono")
    address = models.TextField(verbose_name="Direccion")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Cliente"
        verbose_name_plural = "Clientes"


class Invoice(MainModel, models.Model):
    client = models.ForeignKey(Client, related_name="clients", on_delete=models.CASCADE, verbose_name='Cliente')
    total = models.DecimalField(
        max_digits=10, decimal_places=2, default=0, verbose_name="Total"
    )

    class Meta:
        verbose_name = "Factura"
        verbose_name_plural = "Facturas"

    def __str__(self):
        return f"Factura {self.id} - {self.cliente.nombre}"


class InvoiceDetail(models.Model):
    invoice = models.ForeignKey(Invoice, on_delete=models.CASCADE, verbose_name='Factura')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='Producto')
    quantity = models.PositiveIntegerField(verbose_name="Cantidad")
    precio_unitario = models.DecimalField(
        max_digits=10, decimal_places=2, verbose_name="Precio Unitario"
    )

    class Meta:
        verbose_name = "Detalle de la factura"
        verbose_name_plural = "Detalles de las facturas"

    def subtotal(self):
        return self.quantity * self.precio_unitario

    def __str__(self):
        return f"{self.quantity} x {self.product.name}"
