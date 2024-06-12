from django.db import models

class Booking(models.Model):
    name = models.CharField(max_length=100)
    reservation_date = models.DateField()
    reservation_slot = models.IntegerField(choices=[
        (10, '10 AM'),
        (11, '11 AM'),
        (12, '12 PM'),
        (13, '1 PM'),
        (14, '2 PM'),
        (15, '3 PM'),
        (16, '4 PM'),
        (17, '5 PM'),
        (18, '6 PM'),
        (19, '7 PM'),
        (20, '8 PM'),
    ], default=10)  # set default to 10 AM

    def __str__(self):
        return f"{self.name} - {self.reservation_date} at {self.get_reservation_slot_display()}"
