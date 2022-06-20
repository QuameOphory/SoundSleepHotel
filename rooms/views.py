from django.shortcuts import render
from django.views import generic
from .forms import RoomCreationForm, RoomUpdateForm
from .models import Room
# Create your views here.

class RoomListView(generic.ListView):
    queryset = Room.objects.filter(is_active=True)
    context_object_name = 'rooms'
    template_name = 'rooms/room_list.html'


class RoomCreateView(generic.CreateView):
    form_class = RoomCreationForm
    context_object_name = 'room'
    template_name = 'rooms/room_create.html'


class RoomUpdateView(generic.UpdateView):
    form_class = RoomUpdateForm
    context_object_name = 'room'
    template_name = 'rooms/room_update.html'

