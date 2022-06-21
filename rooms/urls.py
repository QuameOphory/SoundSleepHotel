from django.urls import path
from .views import *


urlpatterns = [
    path('', RoomListView.as_view(), name='room_active'),
    path('all/', AllRoomListView.as_view(), name='room_all'),
    path('occupied/', OccupiedRoomListView.as_view(), name='room_occupied'),
    path('add/', RoomCreateView.as_view(), name='room_add'),
    path('<int:pk>/', RoomDetailView.as_view(), name='room_detail'),
    path('<int:pk>/update', RoomUpdateView.as_view(), name='room_update'),
    path('<int:pk>/delete', RoomDeleteView.as_view(), name='room_delete'),
    path('types/', RoomTypeListView.as_view(), name='roomtype_list'),
    path('types/add', RoomTypeCreateView.as_view(), name='roomtype_create'),
    path('types/<int:pk>/delete/', RoomTypeDeleteView.as_view(), name='roomtype_delete'),
    path('types/<int:pk>/update/', RoomTypeUpdateView.as_view(), name='roomtype_update'),
    path('types/<int:pk>/', RoomTypeDetailView.as_view(), name='roomtype_detail'),
    path('viewtype/<int:pk>/', RoomByTypeListView.as_view(), name='room_type'),
]
