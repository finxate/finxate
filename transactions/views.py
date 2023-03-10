from django.shortcuts import render, redirect
from .models import Transaction
from .forms import TransactionForm

def transactions(request):
    if request.method == 'POST':
        form = TransactionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('transactions')
    else:
        form = TransactionForm()

    transactions = Transaction.objects.all()
    context = {'form': form, 'transactions': transactions}
    return render(request, 'transactions.html', context)

def index(request):
    return render(request, 'transactions/index.html')

def add_transaction(request):
    form = TransactionForm()
    return render(request, 'transactions/transaction_form.html', {'form': form})
