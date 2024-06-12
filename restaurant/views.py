from django.shortcuts import render, redirect
from .models import Booking
from .forms import BookingForm
from django.utils import timezone
from django.http import JsonResponse
from django.core.serializers import serialize

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def menu(request):
    return render(request, 'menu.html')


def all_reservations(request):
    reservations = Booking.objects.all().order_by('reservation_date', 'reservation_slot')
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
                return redirect('make_reservation')  # Redirect to clear form and prevent re-submission
    else:
        form = BookingForm()
    
    reservations = Booking.objects.filter(reservation_date=timezone.now().date())
    return render(request, 'make_reservation.html', {'form': form, 'reservations': reservations})

# Add function to handle AJAX request
def reservations_for_date(request, date):
    reservations = Booking.objects.filter(reservation_date=date).order_by('reservation_slot')
    reservations_json = serialize('json', reservations)
    return JsonResponse(reservations_json, safe=False)