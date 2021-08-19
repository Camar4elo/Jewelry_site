from django.contrib import admin
from shop.models import Material, Category, Decorations, Gems, Images


class ImagesAdmin(admin.StackedInline):
    model = Images


@admin.register(Decorations)
class DecorationsAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'display_gems', 'display_material',
                    'price', 'description')
    list_filter = ('material', 'category', 'price', 'gems')

    inlines = [ImagesAdmin]


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['category']


@admin.register(Material)
class MaterialAdmin(admin.ModelAdmin):
    list_display = ['material']


@admin.register(Gems)
class GemsAdmin(admin.ModelAdmin):
    list_display = ['gems']


@admin.register(Images)
class ImagesAdmin(admin.ModelAdmin):
    list_display = ['decorations', 'display_image']
    list_filter = ['decorations__name', 'decorations__category']
