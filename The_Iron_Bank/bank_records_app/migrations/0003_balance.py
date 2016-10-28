# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-28 03:02
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('bank_records_app', '0002_remove_profile_access_level'),
    ]

    operations = [
        migrations.CreateModel(
            name='Balance',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('num1', models.IntegerField()),
                ('num2', models.IntegerField()),
                ('transaction_type', models.CharField(choices=[('withdraw', 'd'), ('deposit', 'd')], max_length=10)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
