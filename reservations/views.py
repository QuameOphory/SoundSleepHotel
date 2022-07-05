from django.shortcuts import render
from .forms import BookingCreationForm
from django.views import generic
from .models import Booking
# Create your views here.


class BookingCreateView(generic.CreateView):
    form_class =  BookingCreationForm
    context_object_name = 'booking'
    template_name = 'reservations/booking_create.html'


class BookingDetailView(generic.DetailView):
    model = Booking
    context_object_name = 'booking'
    template_name = 'reservations/booking_detail.html'