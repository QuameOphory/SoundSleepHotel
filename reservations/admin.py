from django.contrib import admin
from .models import CheckIn, Booking
# Register your models here.

@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    '''Admin View for Booking'''

    list_display = ('booking_number', 'booking_client', 'booking_from', 'booking_to',)
    list_filter = ('booking_from',)
    search_fields = ('booking_number', 'booking_client',)
    ordering = ('booking_from',)


@admin.register(CheckIn)
class CheckInAdmin(admin.ModelAdmin):
    '''Admin View for CheckIn'''

    list_display = ('checkin_booking', 'funding_id', 'early_checkin',)
    list_filter = ('checkin_booking',)
    search_fields = ('checkin_booking',)
