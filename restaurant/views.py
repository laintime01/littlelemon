from django.shortcuts import render, redirect
from .models import Booking
from .forms import BookingForm
from django.utils import timezone

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def menu(request):
    return render(request, 'menu.html')

def all_reservations(request):
    reservations = Booking.objects.all()
    return render(request, 'all_reservations.html', {'reservations': reservations})

def make_reservation(request):
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            reservation_date = form.cleaned_data['reservation_date']
            reservation_slot = form.cleaned_data['reservation_slot']
            if Booking.objects.filter(reservation_date=reservation_date, reservation_slot=reservation_slot).exists():
                form.add_error('reservation_slot', 'This time slot is already booked.')
            else:
                form.save()
                return redirect('make_reservation')
    else:
        # Use current date as default reservation date
        initial_data = {'reservation_date': timezone.now().date()}
        form = BookingForm(initial=initial_data)
        reservations = Booking.objects.filter(reservation_date=initial_data['reservation_date'])
    return render(request, 'make_reservation.html', {'form': form, 'reservations': reservations})
