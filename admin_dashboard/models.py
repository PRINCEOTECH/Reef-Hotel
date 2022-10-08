from django.db import models
from django.contrib.auth.models import User
from customer.models import Profile


class Customer(models.Model):
    customer = models.ForeignKey(Profile, on_delete=models.CASCADE)
    


    def __str__(self):
        return f"{self.customer} Just joined"



# Create your models here.
