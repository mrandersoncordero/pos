# Django
from django.contrib import admin

# Models
from .models import Category, Unit, Store, Product

admin.site.register(Category)
admin.site.register(Unit)
admin.site.register(Store)
admin.site.register(Product)
