from django.contrib import admin
from .models import Meal, Booking



@admin.register(Meal)
class MealAdmin(admin.ModelAdmin):
    list_display = ['name', 'price']
    

@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ['user', 'meal']
# Register your models here.
