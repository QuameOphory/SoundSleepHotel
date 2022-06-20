from django.db import models
from django.db.models.signals import pre_save
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from numberGenerator import generateRoomNumber
# Create your models here.

class RoomType(models.Model):
    roomtype_code = models.CharField(_("Room Type Code"), max_length=5, unique=True)
    roomtype_name = models.CharField(_("Room Type Name"), max_length=50)
    roomtype_number = models.PositiveIntegerField(_("Total Number of Rooms"))
    roomtype_rate = models.DecimalField(_("Rate"), max_digits=5, decimal_places=2)
    is_active = models.BooleanField(_("Is Active"), default=True)
    created_at = models.DateTimeField(_("Created At"), auto_now_add=True)
    updated_at = models.DateTimeField(_("Updated At"), auto_now=True)
    roomtype_extrainfo = models.TextField(_("Extra Information"), blank=True, null=True)
    

    class Meta:
        verbose_name = _("Room Type")
        verbose_name_plural = _("Room Types")
        ordering = ['is_active', 'roomtype_rate']

    def __str__(self):
        return self.roomtype_name

    def get_absolute_url(self):
        return reverse("roomtype_detail", kwargs={"pk": self.pk})


class Room(models.Model):
    STATUS_CHOICES = [
        ('cv', 'Clean Vacant'),
        ('co', 'Clean Occupied'),
        ('dv', 'Dirty Vacant'),
        ('do', 'Dirty Occupied'),
    ]
    room_number = models.CharField(_("Room Number"), max_length=50, default=_('-'))
    room_type = models.ForeignKey(RoomType, verbose_name=_("Room Type"), on_delete=models.CASCADE, limit_choices_to={'is_active': True})
    room_status = models.CharField(_("Status of Room"), max_length=50, choices=STATUS_CHOICES, default='dv')
    room_dimension = models.DecimalField(_("Room Area"), max_digits=5, decimal_places=2)
    room_totalbeds = models.PositiveIntegerField(_("Number of Beds"), default=1)
    room_totalbaths = models.PositiveIntegerField(_("Number of Baths"), default=1)
    is_active = models.BooleanField(_("Is Active"), default=True) #if room is usable
    is_occupied = models.BooleanField(_("Is Occupied"), default=False)
    created_at = models.DateTimeField(_("Created At"), auto_now_add=True)
    updated_at = models.DateTimeField(_("Updated At"), auto_now=True)
    

    class Meta:
        verbose_name = _("Room")
        verbose_name_plural = _("Rooms")
        ordering = ['room_number']

    def __str__(self):
        return self.room_number

    def get_absolute_url(self):
        return reverse("room_detail", kwargs={"pk": self.pk})

def room_pre_save(sender, instance, *args, **kwargs):
    if instance.id is None:
        prefix = instance.room_type.roomtype_code
        qs = Room.objects.filter(room_type=instance.room_type).order_by('-created_at')
        instance.room_number = generateRoomNumber(qs=qs, prefix=prefix)

pre_save.connect(room_pre_save, sender=Room)