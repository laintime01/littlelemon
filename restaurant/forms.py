from django import forms
from .models import Booking

class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['name', 'reservation_date', 'reservation_slot']
        widgets = {
            'reservation_date': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'reservation_slot': forms.Select(attrs={'class': 'form-control'}),
        }
