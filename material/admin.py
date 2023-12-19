from django.contrib import admin

from material.models import Material


@admin.register(Material)
class MaterialAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'body',)
    list_filter = ('title',)
    search_fields = ('title', 'body',)