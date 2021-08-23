from django.urls import path
from . import views

urlpatterns = [
    path('', views.MainView.as_view(), name='base'),
    path('rings', views.RingsView.as_view(), name='rings'),
    path('earrings', views.EarringsView.as_view(), name='earrings'),
    path('necklaces', views.NecklacesView.as_view(), name='necklaces'),
    path('contacts', views.ContactsView.as_view(), name='contacts'),
]
