from turtle import update
from django.db import models
from django.urls import reverse
from pytz import timezone
import numberGenerator
from django.utils.translation import gettext_lazy as _
from clients.models import Client
from rooms.models import RoomType
import field_validations

# Create your models here.

def generateBookingNumber():
    qs = Booking.objects.order_by('-created_at')
    booking_number = numberGenerator.generateClientNumber(prefix='B', qs=qs)
    return booking_number

class Booking(models.Model):

    booking_number = models.CharField(_("Booking Number"), max_length=50, default=generateBookingNumber)
    booking_client = models.ForeignKey(Client, verbose_name=_("Booking By"), on_delete=models.CASCADE)
    booking_from = models.DateTimeField(_("Booking From"), default=timezone.now, validators=[field_validations.validate_bookingfrom])
    booking_to = models.DateTimeField(_("Booking To"),)
    booking_roomtype = models.ForeignKey(RoomType, verbose_name=_("Room Type"), on_delete=models.CASCADE)
    booking_roomnumber = models.PositiveIntegerField(_("Number of Rooms"), default=1)
    is_active = models.BooleanField(_("Active"), default=True)
    created_at = models.DateTimeField(_("Created At"), auto_now_add=True)
    updated_at = models.DateTimeField(_("Updated At"), auto_now=True)


    class Meta:
        verbose_name = _("Booking")
        verbose_name_plural = _("Bookings")

    def __str__(self):
        return self.booking_number

    def get_absolute_url(self):
        return reverse("booking_detail", kwargs={"pk": self.pk})


class CheckIn(models.Model):

    STATUS_CHOICES = [
        ('checkin', 'Checked In'),
        ('checkout', 'Checked Out'),
        ('unattended', 'Unattended'),
    ]

    checkin_booking = models.ForeignKey(Booking, verbose_name=_("Booking"), on_delete=models.CASCADE)
    booking_status = models.CharField(_("Status"), max_length=20)

    class Meta:
        verbose_name = _("CheckIn")
        verbose_name_plural = _("CheckIns")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("checkin_detail", kwargs={"pk": self.pk})
