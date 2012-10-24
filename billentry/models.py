from django.db import models
from django.contrib.auth.models import User, Group

# Create your models here.

class Purchase(models.Model):
    date = models.DateTimeField('date of purchase')    
    notes = models.CharField(max_length=300)
    payer = models.ForeignKey(User)
    total = models.IntegerField()

class Transaction(models.Model):
    debtor = models.ForeignKey(User)
    amount = models.IntegerField()
    purchase = models.ForeignKey(Purchase)
