from django.contrib import admin
from .models import Room, RoomType

# Register your models here.

@admin.register(Room)
class RoomsAdmin(admin.ModelAdmin):
    '''Admin View for Rooms'''

    list_display = ('room_number', 'room_type', 'room_status', 'room_totalbeds', 'room_totalbaths')
    list_filter = ('room_number', 'room_type')
    search_fields = ('room_number',)


@admin.register(RoomType)
class RoomTypeAdmin(admin.ModelAdmin):
    '''Admin View for RoomType'''

    list_display = ('roomtype_name', 'roomtype_number', 'roomtype_rate',)
    list_filter = ('roomtype_name',)
    search_fields = ('roomtype_name', 'roomtype',)
