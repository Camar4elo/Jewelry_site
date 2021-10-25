from django.shortcuts import render
from django.views.generic.base import View
from .models import Photo, MainPhoto, Category, SocialNetwork, Decoration


class MainView(View):
    def get(self, request):
        photo_and_greetings = MainPhoto.objects.first()
        social_link_instagram = SocialNetwork.objects.get(name='Instagram')
        social_link_whatsapp = SocialNetwork.objects.get(name='Whatsapp')
        social_link_telegram = SocialNetwork.objects.get(name='Telegram')
        social_link_vk = SocialNetwork.objects.get(name='VK')
        category = Category.objects.all()
        images_list = create_images_list(category)
        category_list = create_category_list(category)
        return render(request, "base.html",
                      {"images_list": images_list,
                       "category_list": category_list,
                       "photo_and_greetings": photo_and_greetings,
                       "social_link_instagram": social_link_instagram.link,
                       "social_link_whatsapp": social_link_whatsapp.link,
                       "social_link_telegram": social_link_telegram.link,
                       "social_link_vk": social_link_vk.link})


def create_images_list(category):
    images_list = []
    for category_name in category:
        decorations = Decoration.objects.filter(category_id=category_name.
                                                id).all()
        for decoration in decorations:
            images = Photo.objects.filter(decoration_id=decoration.id)
            data_aos_delay = 0
            for image in images:
                if data_aos_delay == 600:
                    data_aos_delay = 0
                data_aos_delay += 100
                images_list.append({"category": category_name.name,
                                    "name": image.name, "data_aos_delay":
                                    str(data_aos_delay),
                                    "decoration_name": decoration.name})
    return images_list


def create_category_list(category):
    category_list = []
    for category_name in category:
        category_list.append(str(category_name))
    return category_list


class RingsView(View):
    def get(self, request):
        return render(request, "rings.html")


class EarringsView(View):
    def get(self, request):
        return render(request, "earrings.html")


class NecklacesView(View):
    def get(self, request):
        return render(request, "necklaces.html")


class ContactsView(View):
    def get(self, request):
        return render(request, "contacts.html")
