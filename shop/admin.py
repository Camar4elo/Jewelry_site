from django.contrib import admin
from shop.models import Material, Category, Decoration, Gem, Image


class ImageAdmin(admin.StackedInline):
    model = Image


@admin.register(Decoration)
class DecorationAdmin(admin.ModelAdmin):
    fields = ['name', 'category', ('gem', 'material'),
              'price', 'description']
    list_display = ['name', 'category', 'display_gems', 'display_material',
                    'price', 'description', 'display_image']
    list_filter = ['material', 'category', 'price', 'gem']
    inlines = [ImageAdmin]


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name']


@admin.register(Material)
class MaterialAdmin(admin.ModelAdmin):
    list_display = ['name']


@admin.register(Gem)
class GemsAdmin(admin.ModelAdmin):
    list_display = ['name']


@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    list_display = ['decoration', 'display_image']
    list_filter = ['decoration']
