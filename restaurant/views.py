from django.shortcuts import render, redirect
from .forms import BookingForm
from .models import Booking
from django.http import JsonResponse

def booking_list(request):
    bookings = Booking.objects.all()
    return render(request, 'restaurant/booking_list.html', {'bookings': bookings})

def new_booking(request):
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('booking_list')
    else:
        form = BookingForm()
    bookings = Booking.objects.filter(reservation_date=form['reservation_date'].value())
    return render(request, 'restaurant/new_booking.html', {'form': form, 'bookings': bookings})

def bookings_json(request):
    date = request.GET.get('date')
    if date:
        bookings = list(Booking.objects.filter(reservation_date=date).values())
    else:
        bookings = list(Booking.objects.values())
    return JsonResponse(bookings, safe=False)
