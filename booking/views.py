from django.shortcuts import render, redirect
from train.models import Train
from .models import BookedSeat, BookedSeat
from django.contrib import messages
from django.contrib.auth.decorators import login_required
# Create your views here.
@login_required
def seatBook(request, id):
    train = Train.objects.get(pk=id)
    user = request.user
    if user.balance >= train.ticket_price:
        if train.available_seats > 0:
            newBooked = BookedSeat()
            newBooked.train = train
            newBooked.account = user
            user.balance -= train.ticket_price
            user.save()
            newBooked.balance_after_buy = user.balance
            newBooked.save()
            train.available_seats-=1
            train.save()
            return redirect('home')
        else:
            messages.warning(request, "There is no Avilable Seats for this Train")
            return redirect('all_trains')
    else:
        messages.warning(request,"You've no sufficient Balance to Buy the book")
        return redirect('deposit')

