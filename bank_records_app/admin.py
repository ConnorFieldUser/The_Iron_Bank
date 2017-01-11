from django.contrib import admin

from bank_records_app.models import Account, Transaction

# Register your models here.

admin.site.register(Account)
admin.site.register(Transaction)
