from django.contrib import admin
from .models import Room

# Register your models here.

@admin.register(Room)
class RoomsAdmin(admin.ModelAdmin):
    '''Admin View for Rooms'''

    list_display = ('room_number', 'room_type', 'room_status', 'room_totalbeds', 'room_totalbaths')
    list_filter = ('room_number',)
    search_fields = ('room_number',)
