from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from booking.models import Room, Booking


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')
    email = models.EmailField(null=True)
    date_created = models.DateTimeField(default=timezone.now)


    def __str__(self):
        return f'{self.user.username} Profile'






# Create your models here.
