from django.db import models

class Booking(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    number_of_people = models.IntegerField()
    reservation_date = models.DateField()
    reservation_time = models.TimeField()

    def __str__(self):
        return f"{self.name} - {self.reservation_date} {self.reservation_time}"
