from django.urls import path
from .views import seatBook
urlpatterns = [
    path('booked/<int:id>/', seatBook, name='book_seat'),
]
