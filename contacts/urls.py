# contacts/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('new/', views.new_contact, name='new_contact'),
    path('contact/<int:contact_id>/', views.contact_details, name='contact_details'),
]
