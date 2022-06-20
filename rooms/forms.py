from django import forms
from .models import Room, RoomType


class RoomCreationForm(forms.ModelForm):
    class Meta:
        model = Room
        fields = ('room_type', 'room_dimension', 'room_totalbeds', 'room_totalbaths',)


class RoomUpdateForm(forms.ModelForm):
    room_number = forms.CharField(disabled=True)
    class Meta:
        model = Room
        fields = ('room_number', 'room_type', 'room_dimension', 'room_totalbeds', 'room_totalbaths',)


class RoomTypeCreationForm(forms.ModelForm):
    
    class Meta:
        model = RoomType
        fields = ("roomtype_code", "roomtype_name", "roomtype_number", "roomtype_rate", "roomtype_extrainfo",)


class RoomTypeUpdateForm(forms.ModelForm):
    roomtype_code = forms.CharField(disabled=True)
    class Meta:
        model = RoomType
        fields = ('roomtype_code', 'roomtype_number', 'roomtype_name', 'roomtype_rate', 'roomtype_extrainfo',)