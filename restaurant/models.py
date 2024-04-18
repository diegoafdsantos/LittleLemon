from django.db import models

# Create your models here.

class Menu(models.Model):
    id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    inventory = models.IntegerField(default=5)


class Booking(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=255)
    no_of_guests = models.IntegerField(default=6)
    bookingdate = models.DateTimeField()