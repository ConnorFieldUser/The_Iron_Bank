from django.db import models

from django.dispatch import receiver
from django.db.models.signals import post_save


# Create your models here.


class Account(models.Model):

    user = models.OneToOneField('auth.User')
    created = models.DateTimeField(auto_now_add=True)

    @property
    def get_balance(self):
        account_transactions = Transaction.objects.all()
        total = 0
        for transaction in account_transactions:
            if transaction.debit_or_deposit == '+':
                total += transaction.amount
            elif transaction.debit_or_deposit == '-':
                total -= transaction.amount
        return total

    def __str__(self):
        return str(self.user)


@receiver(post_save, sender='auth.User')
def create_user_profile(**kwargs):
    created = kwargs.get('created')
    instance = kwargs.get('instance')
    if created:
        Account.objects.create(user=instance)


DEBIT_OR_DEPOSIT = [
    ('+', 'deposit'),
    ('-', 'withdraw'),
]


class Transaction(models.Model):
    account = models.ForeignKey(Account)
    debit_or_deposit = models.CharField(max_length=1, choices=DEBIT_OR_DEPOSIT)
    amount = models.FloatField()
    created = models.DateTimeField(auto_now_add=True)


# class Deposit(models.Model):
#     account = models.ForeignKey(Account)
#
#
# class Withdraw(models.Model):
#     account = models.ForeignKey(Account)
