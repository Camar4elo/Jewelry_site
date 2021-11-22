from django.contrib import admin
from shop.models import Material, Category, Decoration, Gem, Photo, MainPhoto,\
                        SocialNetwork, MaterialsText, ContactsText,\
                        DeliveryText, PaymentText


class PhotoAdmin(admin.StackedInline):
    model = Photo


@admin.register(Decoration)
class DecorationAdmin(admin.ModelAdmin):
    fields = ['name', 'category', ('gem', 'material'),
              'price', 'description']
    list_display = ['name', 'category', 'display_gems', 'display_material',
                    'price', 'description', 'display_images']
    list_filter = ['material', 'category', 'price', 'gem']
    inlines = [PhotoAdmin]


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name']


@admin.register(Material)
class MaterialAdmin(admin.ModelAdmin):
    list_display = ['name']


@admin.register(Gem)
class GemsAdmin(admin.ModelAdmin):
    list_display = ['name', 'choice']


@admin.register(Photo)
class PhotoAdmin(admin.ModelAdmin):
    list_display = ['decoration', 'display_image']
    list_filter = ['decoration']


@admin.register(MainPhoto)
class MainPhotoAdmin(admin.ModelAdmin):
    list_display = ['greetings', 'main_photo', 'display_image']


@admin.register(SocialNetwork)
class SocialNetworkAdmin(admin.ModelAdmin):
    list_display = ['name', 'link']


@admin.register(MaterialsText)
class MaterialsTextAdmin(admin.ModelAdmin):
    list_display = ['content']


@admin.register(ContactsText)
class ContactsTextAdmin(admin.ModelAdmin):
    list_display = ['content']


@admin.register(DeliveryText)
class DeliveryTextAdmin(admin.ModelAdmin):
    list_display = ['content']


@admin.register(PaymentText)
class PaymentTextAdmin(admin.ModelAdmin):
    list_display = ['content']
