from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import DishCategory, Dish, Gallery, Events, Chefs, Contacts
from .forms import ReservationForm
from django.views.generic import TemplateView
from django.contrib import messages

# Create your views here.
class IndexView(TemplateView):
    template_name = 'main.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        categories = DishCategory.objects.filter(is_visible=True)
        gallery = Gallery.objects.all()
        events = Events.objects.all()
        chefs = Chefs.objects.all()
        contact = Contacts.objects.first()
        form = ReservationForm()

        context['categories'] = categories
        context['gallery'] = gallery
        context['events'] = events
        context['chefs'] = chefs
        context['contact'] = contact
        context['form'] = form
        context['title_menu'] = 'Check Our <span>Yummy Menu</span>'
        context['title_gallery'] = 'Check <span>Our Gallery</span>'
        context['title_events'] = 'Share <span>Your Moments</span> In Our Restaurant'
        context['title_chefs'] = 'Our <span>Proffesional</span> Chefs'
        context['title_contacts'] = 'Need Help? <span>Contact Us</span>'
        context['title_contacts_address'] = 'Our Address'
        context['title_contact_email'] = 'Email Us'
        context['title_contact_phone'] = 'Call Us'
        context['title_contact_time'] = 'Opening Hours'

        return context

    def post(self, request):
        form = ReservationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Ваше бронирование принято')
            return redirect('main:index')

def manager(request):
    ...