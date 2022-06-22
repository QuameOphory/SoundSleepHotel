from django import forms
from .models import Booking, CheckIn
from datetime import timedelta, date
from django.forms import ValidationError
from django.utils.translation import gettext_lazy as _
import pytz

utc = pytz.UTC

class BookingCreationForm(forms.ModelForm):
    
    class Meta:
        model = Booking
        fields = ("booking_client", "booking_roomtype", "booking_from", "booking_to", "booking_roomnumber",)

    def clean_booking_from(self):
        data = self.cleaned_data["booking_from"]
        if data < date.today():
            raise ValidationError(_('You are trying to book for a date which is in the past. \nKindly check your date and correct it.'))
        return data
    
    def clean_booking_to(self):
        data = self.cleaned_data["booking_to"]
        if data < date.today():
            raise ValidationError(_('This date cannot be a past date.'))
        return data

    def clean(self):
        cleaned_data = super().clean()
        booking_from = cleaned_data.get('booking_from')
        booking_to = cleaned_data.get('booking_to')
        if booking_to and booking_from:
            if booking_from > booking_to:
                raise ValidationError(_('Booking Start Date cannot be after Booking End Date'))
        return cleaned_data