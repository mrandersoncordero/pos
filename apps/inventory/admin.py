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
                'name', 'description'
            ),
        }),
        ('Metadata', {
            'fields': (
                ('created', 'modified'),
            )
        })
    )
    
    readonly_fields = ('created', 'modified')

admin.site.register(Unit)
admin.site.register(Store)
admin.site.register(Product)
