from django import forms
from .models import Room


class RoomCreationForm(forms.ModelForm):
    class Meta:
        model = Room
        fields = ('room_type', 'room_dimension', 'room_totalbeds', 'room_totalbaths',)


class RoomUpdateForm(forms.ModelForm):
    room_number = forms.CharField(disabled=True)
    class Meta:
        model = Room
        fields = ('room_number', 'room_type', 'room_dimension', 'room_totalbeds', 'room_totalbaths',)

