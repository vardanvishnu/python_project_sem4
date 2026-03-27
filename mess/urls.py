from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('book/<int:meal_id>/', views.book_meal, name='book'),
    path('my-booking/', views.my_booking, name='my_booking'),
    
]