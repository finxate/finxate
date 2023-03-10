from django.db import models
class Transaction(models.Model):
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    note = models.CharField(max_length=255)
    transaction_type = models.CharField(max_length=10, choices=[('credit', 'Credit'), ('debit', 'Debit')])
    date = models.DateField()
    category = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.amount} ({self.transaction_type})'

