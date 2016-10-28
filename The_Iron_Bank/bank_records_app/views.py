# from django.shortcuts import render

from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import ListView, TemplateView
from django.views.generic.edit import CreateView

from bank_records_app.models import Transaction

# Create your views here.


class UserCreateView(CreateView):
    model = User
    form_class = UserCreationForm
    success_url = "/"


class IndexView(TemplateView):
        template_name = 'index.html'


class TransactionView(ListView):
    template_name = 'transactions.html'
    model = Transaction
