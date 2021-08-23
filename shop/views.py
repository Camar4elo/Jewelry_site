from django.shortcuts import render
from django.views.generic.base import View


class MainView(View):
    def get(self, request):
        return render(request, "index.html")


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