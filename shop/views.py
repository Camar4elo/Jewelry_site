from django.shortcuts import render, redirect
from django.views.generic.base import View
from .models import Photo, MainPhoto, Category, SocialNetwork, Decoration, Gem, MaterialsText, ContactsText,\
                    DeliveryText, PaymentText
from .forms import ContactMe
from bot.bot import send_visitor_message
import math


class MainView(View):
    def get(self, request):
        main_photo = MainPhoto.objects.values('photo').first()
        main_text = MainPhoto.objects.values('content').first()
        social_networks = SocialNetwork.objects.all()
        images_list = create_images_list()
        category_list = create_category_list()
        gems_list = create_gems_list()
        materials_text = MaterialsText.objects.first()
        contacts_text = ContactsText.objects.first()
        delivery_text = DeliveryText.objects.first()
        payment_text = PaymentText.objects.first()
        form = ContactMe(request.GET)
        return render(request, "base.html",
                      {"images_list": images_list,
                       "category_list": category_list,
                       "main_photo": main_photo,
                       "social_networks": social_networks,
                       "form": form,
                       "gems_list": gems_list,
                       "main_text": main_text,
                       "materials_text": materials_text,
                       "contacts_text": contacts_text,
                       "delivery_text": delivery_text,
                       "payment_text": payment_text})

    def post(self, request):
        form = ContactMe(request.POST)
        if form.is_valid():
            name = form.data['name']
            phone = form.data['phone_number']
            message = form.data['message']
            bot_message = f'Имя: {name}\nТелефон: {phone}\nСообщение: {message}'
            send_visitor_message(bot_message)
            return redirect("base")


def create_images_list():
    """
    Makes a query to the db. Forms a list with jewelry images and data_aos_delay value.
    Data_aos_delay refers to the JS AOS library, responsible for the animation speed.
    """
    category = Category.objects.all()
    images_list = []
    for category_name in category:
        decorations = Decoration.objects.filter(category_id=category_name.id).all()
        data_aos_delay = 0
        for decoration in decorations:
            images = Photo.objects.filter(decoration_id=decoration.id)
            for image in images:
                if data_aos_delay == 600:
                    data_aos_delay = 0
                data_aos_delay += 100
                images_list.append({"category": category_name.name,
                                    "name": image.photo,
                                    "data_aos_delay": str(data_aos_delay),
                                    "decoration_name": decoration.name})
    return images_list


def create_category_list():
    """Makes a query to the db. Forms a list with jewelry categories"""
    category = Category.objects.all()
    category_list = []
    for category_name in category:
        category_list.append(str(category_name))
    return category_list


def create_gems_list():
    """Makes a query to the db. Forms a list with gems."""
    initial_value = 0
    end_value = 4
    gems = Gem.objects.all()
    # used to form the numbers of html tag <ul>, including no more than 4 tags <li>
    lists_amount = int(math.ceil(len(gems)/end_value))
    gems_list = []
    for i in range(lists_amount):
        gems_list.append(gems[initial_value:end_value])
        initial_value = end_value
        end_value += 4
    return gems_list
