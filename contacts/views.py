# contacts/views.py
from django.shortcuts import render, redirect, get_object_or_404
from .models import Contact
from .forms import ContactForm

def home(request):
    contacts = Contact.objects.all()
    return render(request, 'contacts/home.html', {'contacts': contacts})

