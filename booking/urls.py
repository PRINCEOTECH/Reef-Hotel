from django.urls import path
from .views import BookingListView, RoomDetailView, RooomListView, BookingView, CancelBookingView
app_name = 'booking'



urlpatterns = [
    path('room_list/', RooomListView, name='RoomListView'),
    path('booking_list/', BookingListView.as_view(), name='BookingListView'),
    path('book/', BookingView.as_view(), name='BookingView'),
    path('room/<str:category>/', RoomDetailView.as_view(), name='RoomDetailView'),
    path('booking/cancel/<pk>', CancelBookingView.as_view(), name='CancelBookingView'),
]