from django.shortcuts import render, redirect
from .models import Transaction
from .forms import TransactionForm
from django.contrib.auth.decorators import login_required
# Create your views here.
@login_required
def deposit_view(request):
    form = TransactionForm()
    if request.method == 'POST':
        form = TransactionForm(request.POST)
        if form.is_valid():
            deposit_amount = form.cleaned_data['amount']
            deposit = Transaction.objects.create(
                account=request.user,
                amount= deposit_amount
            )
            deposit.save()
            request.user.balance+=deposit_amount
            request.user.save()
            return redirect('home')
    return render(request, 'deposit_form.html',{'form': form, 'type': 'Deposit'})