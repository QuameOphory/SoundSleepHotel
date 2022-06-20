from django.urls import path
from .views import *

urlpatterns = [
    path('', RoomListView.as_view(), name='room_active'),
    path('all/', AllRoomListView.as_view(), name='room_all'),
    path('occupied/', OccupiedRoomListView.as_view(), name='room_occupied'),
    path('add/', RoomCreateView.as_view(), name='room_add'),
    path('<int:pk>/', RoomDetailView.as_view(), name='room_detail'),
    path('<int:pk>/update', RoomUpdateView.as_view(), name='room_update'),
]
