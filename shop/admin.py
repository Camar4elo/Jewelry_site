from django.contrib import admin
from shop.models import Material, Category, Decorations


@admin.register(Decorations)
class DecorationsAdmin(admin.ModelAdmin):
    list_display = ['name']
    list_filter = ['material', 'category']


@admin.register(Material)
class MaterialAdmin(admin.ModelAdmin):
    list_display = ['material']


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['category']
