# from django.shortcuts import render

from rest_framework.generics import ListCreateAPIView

from bank_records_app.serializers import TransactionSerializer

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

    def get_queryset(self):
        return Transaction.objects.filter(user=self.request.user)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['transactions'] = Transaction.objects.filter(user=self.request.user)
        return context


# API Views

# class TransactionListCreateAPIView(ListCreateAPIView):
#     queryset = Transaction.objects.all()
#     serializer_class = TransactionSerializer
#
#     def perform_create(self, serializer):
#         # print(serializer)
#         # print(serializer.data)
#         serializer.save(created_by=self.request.user)
#         return super().perform_create(serializer)


class TransactionListAPIView(ListCreateAPIView):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer
