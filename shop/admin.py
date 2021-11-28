from django.contrib import admin
from shop.models import Material, Category, Decoration, Gem, Photo, MainPhoto, SocialNetwork, MaterialsText,\
                        ContactsText, DeliveryText, PaymentText
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib import messages


class PhotoAdmin(admin.StackedInline):
    model = Photo


@admin.register(Decoration)
class DecorationAdmin(admin.ModelAdmin):
    fields = ['name', 'category', ('gem', 'material'), 'description']
    list_display = ['name', 'category', 'display_gems', 'display_material', 'description', 'display_images']
    list_filter = ['material', 'category', 'gem']
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

    def add_view(self, request):
        if self.model.objects.count() == 1:
            self.message_user(request, 'Можно создать не более одной записи', messages.ERROR)
            return HttpResponseRedirect(reverse(f'admin:{self.model._meta.app_label}_mainphoto_changelist'))
        return super().add_view(request)


@admin.register(SocialNetwork)
class SocialNetworkAdmin(admin.ModelAdmin):
    list_display = ['name', 'link', 'svg_link']


@admin.register(MaterialsText)
class MaterialsTextAdmin(admin.ModelAdmin):
    list_display = ['content']

    def add_view(self, request):
        if self.model.objects.count() == 1:
            self.message_user(request, 'Можно создать не более одной записи', messages.ERROR)
            return HttpResponseRedirect(reverse(f'admin:{self.model._meta.app_label}_materialstext_changelist'))
        return super().add_view(request)


@admin.register(ContactsText)
class ContactsTextAdmin(admin.ModelAdmin):
    list_display = ['content']

    def add_view(self, request):
        if self.model.objects.count() == 1:
            self.message_user(request, 'Можно создать не более одной записи', messages.ERROR)
            return HttpResponseRedirect(reverse(f'admin:{self.model._meta.app_label}_contactstext_changelist'))
        return super().add_view(request)


@admin.register(DeliveryText)
class DeliveryTextAdmin(admin.ModelAdmin):
    list_display = ['content']

    def add_view(self, request):
        if self.model.objects.count() == 1:
            self.message_user(request, 'Можно создать не более одной записи', messages.ERROR)
            return HttpResponseRedirect(reverse(f'admin:{self.model._meta.app_label}_deliverytext_changelist'))
        return super().add_view(request)


@admin.register(PaymentText)
class PaymentTextAdmin(admin.ModelAdmin):
    list_display = ['content']

    def add_view(self, request):
        if self.model.objects.count() == 1:
            self.message_user(request, 'Можно создать не более одной записи', messages.ERROR)
            return HttpResponseRedirect(reverse(f'admin:{self.model._meta.app_label}_paymenttext_changelist'))
        return super().add_view(request)
