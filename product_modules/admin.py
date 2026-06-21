from django.contrib import admin
from . import models
# Register your models here.

class ProductAdmin(admin.ModelAdmin):
    list_display = ['__str__','price', 'is_active']
    list_editable = ['price', 'is_active']
    list_filter = ['category','product_brand']

admin.site.register(models.Product, ProductAdmin)
admin.site.register(models.ProductCategory)
admin.site.register(models.ProductTag)
admin.site.register(models.ProductBrand)


