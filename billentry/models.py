from django.db import models
from django.contrib.auth.models import User, Group

# Create your models here.

class Settlement(models.Model):
    date = models.DateTimeField('date of settlement')

class Bill(models.Model):
    amount = models.IntegerField()
    date = models.DateTimeField('date of bill')
    payer = models.ForeignKey(User)
    beneficiary = models.ForeignKey(Group)
    notes = models.CharField(max_length=300)
    settlement = models.ForeignKey(Settlement)

class Payment(models.Model):
    payer = models.ForeignKey(User, related_name='payment_paid_set')
    recipient = models.ForeignKey(User, related_name='payment_received_set')
    amount = models.IntegerField()
    settlement = models.ForeignKey(Settlement)
