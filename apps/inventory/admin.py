# Django
from django.contrib import admin

# Models
from .models import Category, Unit, Store, Product

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'description', 'active']
    list_display_links = ['id']
    list_editable = ['name']
    list_filter = ['name', 'created']
    search_fields = ['name']
    ordering = ['created']

    fieldsets = (
        ('Categoria', {
            "fields": (
                'name', 'description', 'active'
            ),
        }),
        ('Metadata', {
            'fields': (
                ('created', 'modified'),
            )
        })
    )
    
    readonly_fields = ('created', 'modified')


@admin.register(Product)
class ModelAdmin(admin.ModelAdmin):
    list_display = ['name', 'category', 'unit', 'store', 'stock', 'price_sale']
    list_display_links = ['name']
    list_filter = ['created', 'category__name']
    search_fields = ['name', 'category__name']
    ordering = ['created']

    fieldsets = (
        ('Informacion', {
            "fields": (
                'name', 'description',
                ('category', 'unit', 'store', 'active'),
                ('stock', 'purchase_price', 'price_sale'),
            ),
        }),
        ('Metadata', {
            'fields': (
                ('created', 'modified'),
            )
        })
    )
    
    readonly_fields = ('created', 'modified')

@admin.register(Unit)
class UnitAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'description', 'quantity', 'created']
    list_display_links = ['id']
    list_editable = ['name', 'quantity']
    list_filter = ['name', 'created']
    search_fields = ['name', 'created']
    
    fieldsets = (
        ('Informacion', {
            "fields": (
                'name', 'description', 'quantity'     
            ),
        }),
        ('Metadata', {
            'fields': (
                ('created', 'modified'),
            )
        })
    )
    
    readonly_fields = ('created', 'modified')
    
@admin.register(Store)
class StoreAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'address', 'created']
    list_display_links = ['id']
    list_editable = ['name']
    list_filter = ['name', 'created']
    search_fields = ['id', 'name']

    fieldsets = (
        (None, {
            "fields": (
                'name', 'address'
            ),
        }),
        ('Metadata', {
            'fields': (
                ('created', 'modified'),
            )
        })
    )
    
    readonly_fields = ('created', 'modified')

