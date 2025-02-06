# Django
from django.contrib import admin
# Models
from .models import Client, Invoice, InvoiceDetail

class InvoiceDetailInline(admin.TabularInline):
    model = InvoiceDetail
    extra = 1

class FacturaAdmin(admin.ModelAdmin):
    inlines = [InvoiceDetailInline]
    list_display = ['id', 'client', 'created', 'total']

admin.site.register(Client)
admin.site.register(Invoice, FacturaAdmin)
