from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('menu/', views.menu, name='menu'),
    path('make_reservation/', views.make_reservation, name='make_reservation'),
    path('reservations/', views.all_reservations, name='all_reservations'),
    path('reservations_for_date/<str:date>/', views.reservations_for_date, name='reservations_for_date'),
]
