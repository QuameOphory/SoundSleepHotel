from django.db.models.signals import post_save, m2m_changed
from django.db import models
from django.urls import reverse
from django.utils import timezone
import numberGenerator
from django.utils.translation import gettext_lazy as _
from clients.models import Client, ClientFunding
from rooms.models import RoomType, Room
import field_validations

# Create your models here.

def generateBookingNumber():
    qs = Booking.objects.order_by('-created_at')
    booking_number = numberGenerator.generateBookingNumber(qs=qs)
    return booking_number

class Booking(models.Model):

    STATUS_CHOICES = [
        ('checkin', 'Checked In'),
        ('checkout', 'Checked Out'),
        ('unattended', 'Unattended'),
        ('cancel', 'Cancel'),
    ]

    booking_number = models.CharField(_("Booking Number"), max_length=50, default=generateBookingNumber)
    booking_client = models.ForeignKey(Client, verbose_name=_("Booking By"), on_delete=models.CASCADE)
    booking_from = models.DateTimeField(_("Booking From"), validators=[field_validations.validate_bookingfrom], default=timezone.now)
    booking_to = models.DateTimeField(_("Booking To"),)
    booking_roomtype = models.ForeignKey(RoomType, verbose_name=_("Room Type"), on_delete=models.CASCADE)
    booking_roomnumber = models.PositiveIntegerField(_("Number of Rooms"), default=1)
    is_active = models.BooleanField(_("Active"), default=True)
    created_at = models.DateTimeField(_("Created At"), auto_now_add=True)
    updated_at = models.DateTimeField(_("Updated At"), auto_now=True)
    booking_status = models.CharField(_("Status"), max_length=20, default='unattended')


    class Meta:
        verbose_name = _("Booking")
        verbose_name_plural = _("Bookings")

    def __str__(self):
        return self.booking_client.get_fullname()

    def get_absolute_url(self):
        return reverse("booking_detail", kwargs={"pk": self.pk})

def booking_post_save(sender, instance, created, *args, **kwargs):
    if created:
        number_of_rooms = instance.booking_roomnumber
        for i in range(0,number_of_rooms-1):
            Booking.objects.create(
                booking_roomtype=instance.booking_roomtype,
                booking_client = instance.booking_client,
                booking_from = instance.booking_from,
                booking_to = instance.booking_to,
                booking_roomnumber = 1
            )
post_save.connect(booking_post_save, sender=Booking)

class CheckIn(models.Model):

    
    CHECKIN_KIND_CHOICES = [
        ('hd', 'Half Day'),
        ('re', 'Regular Check-in'),
    ]
    funding_id = models.ForeignKey(ClientFunding, verbose_name=_("Funding Account"), on_delete=models.CASCADE)
    checkin_booking = models.OneToOneField(Booking, verbose_name=_("Booking"), on_delete=models.CASCADE)
    checkin_time = models.DateTimeField(_("Check-in At"), default=timezone.now)
    checkin_type = models.CharField(_("Check-in Type"), max_length=4, choices=CHECKIN_KIND_CHOICES, default='re')
    early_checkin = models.BooleanField(_("Early Check-in"), default=False)
    room = models.OneToOneField(Room, verbose_name=_("Rooms"), on_delete=models.CASCADE, null=True)

    class Meta:
        verbose_name = _("Check In")
        verbose_name_plural = _("Check Ins")

    def __str__(self):
        return f'{self.checkin_booking}'

    def get_absolute_url(self):
        return reverse("checkin_detail", kwargs={"pk": self.pk})

    @property
    def get_booking_number(self):
        return str(self.checkin_booking.booking_number)


# def rooms_changed(sender, pk_set, **kwargs):
#     for i in pk_set:
#         room = Room.objects.get(pk=i)
#         room.is_occupied = True
#         room.save()

# m2m_changed.connect(rooms_changed, sender=CheckIn.rooms.through)

def checkin_post_save(sender, instance, created, *args, **kwargs):
    if created:
        instance.room.is_occupied = True
        instance.room.save()

post_save.connect(checkin_post_save, sender=CheckIn)