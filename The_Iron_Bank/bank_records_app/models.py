from django.db import models

from django.dispatch import receiver
from django.db.models.signals import post_save

# Create your models here.


TRANSACTION_TYPE = [
    ('withdraw', 'd'),
    ('deposit', 'd')
]


class Balance(models.Model):
    user = models.ForeignKey('auth.User')
    created = models.DateTimeField(auto_now_add=True)
    num1 = models.IntegerField()
    num2 = models.IntegerField()
    transaction_type = models.CharField(max_length=10, choices=TRANSACTION_TYPE)

    @property
    def deposit(self):
        num1, num2 = [self.operator, self.num1, self.num2]
        return num1 + num2

    @property
    def withdraw(self):
        num1, num2 = [self.operator, self.num1, self.num2]
        return num1 + num2


class Profile(models.Model):
    user = models.OneToOneField('auth.User')


@receiver(post_save, sender='auth.User')
def create_user_profile(**kwargs):
    created = kwargs.get('created')
    instance = kwargs.get('instance')
    if created:
        Profile.objects.create(user=instance)

    def __str__(self):
        return self.username
