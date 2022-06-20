from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.views import generic
from .forms import RoomCreationForm, RoomUpdateForm, RoomTypeCreationForm, RoomTypeUpdateForm
from .models import Room, RoomType
from django.http import HttpResponseRedirect
# Create your views here.

class RoomListView(generic.ListView):
    queryset = Room.objects.filter(is_active=True)
    context_object_name = 'rooms'
    template_name = 'rooms/room_list.html'


class AllRoomListView(generic.ListView):
    queryset = Room.objects.all()
    context_object_name = 'rooms'
    template_name = 'rooms/room_list.html'

class OccupiedRoomListView(generic.ListView):
    queryset = Room.objects.filter(is_occupied=True)
    context_object_name = 'rooms'
    template_name = 'rooms/room_list.html'


class RoomCreateView(generic.CreateView):
    form_class = RoomCreationForm
    context_object_name = 'room'
    template_name = 'rooms/room_create.html'


class RoomUpdateView(generic.UpdateView):
    form_class = RoomUpdateForm
    model = Room
    template_name = 'rooms/room_create.html'


class RoomDetailView(generic.DetailView):
    context_object_name = 'room'
    model = Room
    template_name = 'rooms/room_detail.html'


class RoomDeleteView(generic.DeleteView):
    model = Room
    context_object_name = 'room'
    success_url = reverse_lazy('room_all')


class RoomTypeListView(generic.ListView):
    queryset = RoomType.objects.filter(is_active=True)
    context_object_name = 'roomtypes'
    template_name = 'room/roomtype_list.html'


class AllRoomTypeListView(generic.ListView):
    queryset = RoomType.objects.all()
    context_object_name = 'roomtypes'
    template_name = 'room/roomtype_list.html'


class RoomTypeDeleteView(generic.DeleteView):
    model = RoomType
    context_object_name = 'roomtype'
    success_url = reverse_lazy('roomtype_list5/')
    

class RoomTypeDetailView(generic.DetailView):
    context_object_name = 'roomtype'
    model = RoomType
    template_name = 'rooms/roomtype_detail.html'


class RoomTypeCreateView(generic.CreateView):
    form_class = RoomTypeCreationForm
    template_name = 'rooms/roomtype_create.html'
    context_object_name = 'room'


class RoomTypeUpdateView(generic.UpdateView):
    form_class = RoomTypeUpdateForm
    model = RoomType
    template_name = 'rooms/roomtype_create.html'
    context_object_name = 'room'