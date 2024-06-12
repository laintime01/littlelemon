from django.urls import path
from . import views

urlpatterns = [
    path('', views.booking_list, name='booking_list'),
    path('new/', views.new_booking, name='new_booking'),
    path('bookings_json/', views.bookings_json, name='bookings_json'),
]
