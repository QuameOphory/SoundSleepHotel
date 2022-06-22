from django.urls import path
from .views import *

urlpatterns = [
    path('add/', BookingCreateView.as_view(), name='booking_create'),
]
