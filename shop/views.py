from django.shortcuts import render, redirect
from django.views.generic.base import View
from .models import Photo, MainPhoto, Category, SocialNetwork, Decoration, \
                    Gem
from .forms import ContactMe
from bot.bot import send_visitor_message
import math


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
        gems_list = create_gems_list()
        form = ContactMe(request.GET)
        return render(request, "base.html",
                      {"images_list": images_list,
                       "category_list": category_list,
                       "photo_and_greetings": photo_and_greetings,
                       "social_link_instagram": social_link_instagram.link,
                       "social_link_whatsapp": social_link_whatsapp.link,
                       "social_link_telegram": social_link_telegram.link,
                       "social_link_vk": social_link_vk.link,
                       "form": form,
                       "gems_list": gems_list})

    def post(self, request):
        form = ContactMe(request.POST)
        if form.is_valid():
            name = form.data['name']
            phone = form.data['phone_number']
            message = form.data['message']
            bot_message = f'Имя: {name}\nТелефон: {phone}'\
                          f'\nСообщение: {message}'
            send_visitor_message(bot_message)
            return redirect("base")


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
                                    "name": image.name,
                                    "data_aos_delay": str(data_aos_delay),
                                    "decoration_name": decoration.name})
    return images_list


def create_category_list(category):
    category_list = []
    for category_name in category:
        category_list.append(str(category_name))
    return category_list


def create_gems_list():
    initial_value = 0
    end_value = 4
    gems = Gem.objects.all()
    lists_amount = int(math.ceil(len(gems)/end_value))
    gems_list = []
    len_value = 0
    for result in range(lists_amount):
        res_list = []
        for gem in gems[initial_value:end_value]:
            res_list.append(gem)
            len_value += 1
        initial_value = end_value
        end_value += 4
        gems_list.append(res_list)
    return gems_list


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
