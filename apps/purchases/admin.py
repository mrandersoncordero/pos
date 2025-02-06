# Django
from django.contrib import admin

# Models
from .models import Provider, Purchase, PurchaseDetail


@admin.register(Provider)
class ProviderAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'phone', 'address']
    
class PurchaseDetailInline(admin.TabularInline):
    model = PurchaseDetail
    extra = 1

class PurchaseAdmin(admin.ModelAdmin):
    inlines = [PurchaseDetailInline]
    list_display = ['id', 'provider', 'created', 'total']

admin.site.register(Purchase, PurchaseAdmin)
