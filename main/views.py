from django.shortcuts import render
from django.http import HttpResponse
from .models import DishCategory, Dish, Gallery, Events, Chefs, Contacts


# Create your views here.
def index(request):
    categories = DishCategory.objects.filter(is_visible=True)
    gallery = Gallery.objects.all()
    events = Events.objects.all()
    chefs = Chefs.objects.all()
    contact = Contacts.objects.first()

    context = {
        'title_menu': 'Check Our <span>Yummy Menu</span>',
        'title_gallery': 'Check <span>Our Gallery</span>',
        'title_events': 'Share <span>Your Moments</span> In Our Restaurant',
        'title_chefs': 'Our <span>Proffesional</span> Chefs',
        'title_contacts': 'Need Help? <span>Contact Us</span>',
        'title_contacts_address': 'Our Address',
        'title_contact_email': 'Email Us',
        'title_contact_phone': 'Call Us',
        'title_contact_time': 'Opening Hours',
        'categories': categories,
        'gallery': gallery,
        'events': events,
        'chefs': chefs,
        'contact': contact
    }

    return render(request, 'main.html', context=context)

def manager(request):
    ...