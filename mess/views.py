
from django.shortcuts import render, redirect
from .models import Meal, Booking
from django.contrib.auth.decorators import login_required

def home(request):
    meals = Meal.objects.all()
    return render(request, 'home.html', {'meals': meals})

@login_required
def book_meal(request, meal_id):
    meal = Meal.objects.get(id=meal_id)
    Booking.objects.create(user=request.user, meal=meal)
    return redirect('my_booking')

@login_required
def my_booking(request):
    bookings = Booking.objects.filter(user=request.user)
    return render(request, 'bookings.html', {'bookings': bookings})



# Create your views here.
