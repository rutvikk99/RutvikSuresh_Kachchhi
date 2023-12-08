# contacts/views.py
from django.shortcuts import render, redirect, get_object_or_404
from .models import Contact
from .forms import ContactForm

def home(request):
    contacts = Contact.objects.all()
    return render(request, 'contacts/home.html', {'contacts': contacts})

def new_contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = ContactForm()
    
    return render(request, 'contacts/new_contact.html', {'form': form})

def contact_details(request, contact_id):
    contact = get_object_or_404(Contact, pk=contact_id)
    return render(request, 'contacts/contact_details.html', {'contact': contact})