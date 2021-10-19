from django.shortcuts import render
from django.views.generic.base import View
from .models import Photo


class MainView(View):
    def get(self, request):
        images = Photo.objects.all()
        images_list = create_images_list(images)
        return render(request, "base.html", {"images_list": images_list})


def create_images_list(images):
    images_list = []
    data_aos_delay = 0
    for image in images:
        if data_aos_delay == 600:
            data_aos_delay = 0
        data_aos_delay += 100
        images_list.append({"name": image.name, "data_aos_delay":
                           str(data_aos_delay)})
    return images_list


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
