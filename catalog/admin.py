from django.contrib import admin

from catalog.models import Product, Category, Version


# admin.site.register(Category)

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'price', 'category',)
    list_filter = ('category',)
    search_fields = ('name', 'description',)

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'category_name',)
    list_filter = ('id',)
    search_fields = ('category_name',)

@admin.register(Version)
class VersionAdmin(admin.ModelAdmin):
    list_display = ('product_name', 'number', 'title', 'current',)
    list_filter = ('current',)


