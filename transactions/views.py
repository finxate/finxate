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

def transactions_list(request):
    context = {'transactions': Transaction.objects.all()}
    return render(request, 'transactions/transactions_list.html', context)

def insert_transaction(request):
    form = TransactionForm(request.POST)
    amount = request.POST.get('amount')
    note = request.POST.get('note')
    transaction_type = request.POST.get('transaction_type')
    date = request.POST.get('date')
    category = request.POST.get('category')
    transaction = Transaction(amount=amount, note=note, transaction_type=transaction_type, date=date, category=category)
    transaction.save()
    return redirect('/transactions/list/')