"""The_Iron_Bank URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin

from bank_records_app.views import UserCreateView, IndexView, TransactionView, TransactionListCreateAPIView, \
                                   TransactionCreateView, TransactionDetailAPIView

from rest_framework.authtoken.views import obtain_auth_token


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url('^', include('django.contrib.auth.urls')),
    url(r'^obtain-token/$', obtain_auth_token),
    url(r'^$', IndexView.as_view(), name="index_view"),
    url(r'^create_user/$', UserCreateView.as_view(), name="user_create_view"),
    url(r'^user_transactions/$', TransactionView.as_view(), name="transactions"),
    url(r'^create_transaction/$', TransactionCreateView.as_view(), name="user_transaction_create_view"),
    # API URLs
    url(r'^transactions_api/$', TransactionListCreateAPIView.as_view(), name="transaction_list_create_api_view"),
    url(r'^transaction/(?P<pk>\d+)/$', TransactionDetailAPIView.as_view(), name="transaction_detail_api_view")
]
