from django.db import models
from django.conf import settings
from django.urls import reverse_lazy



class Room(models.Model):
    ROOM_CATEGORIES = (
        ('DH', 'DELUXE-HOTEL'),
        ('KH', 'KING-HOTEL'),
        ('LH', 'LUXE-HOTEL'),
        ('FSH', 'FIVE-STAR-HOTEL'),
    )
    room_number = models.IntegerField()
    category = models.CharField(max_length=20, choices=ROOM_CATEGORIES)

    def __str__(self):
        return f"Room {self.room_number} Of {self.category}"



class Booking(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    check_in_date = models.DateField()
    check_in_time = models.TimeField()
    check_out_date = models.DateField()
    check_out_time = models.TimeField()
    beds = models.IntegerField()
    number_of_occupant = models.IntegerField()

    def __str__(self):
        return f"{self.user} Has Booked ||{self.room} With {self.beds} Bed For {self.number_of_occupant} Person/People From Date:{self.check_in_date} Time:{self.check_in_time} To Date:{self.check_out_date} Time{self.check_out_time} "


    def get_room_category(self):
        room_categories = dict(self.room.ROOM_CATEGORIES)
        room_category = room_categories.get(self.room.category)
        return room_category

    def get_cancel_booking_url(self):
        return reverse_lazy('booking:CancelBookingView', args=[self.pk,])

# Create your models here.
