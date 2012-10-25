from django.db import models
from django.contrib.auth.models import User, Group


class Payment(models.Model):
    date = models.DateTimeField('date of purchase')    
    notes = models.CharField(max_length=300)
    payer = models.ForeignKey(User)
    total = models.IntegerField()

    def __unicode__(self):
        return self.payer.get_full_name() + " paid " + self.get_total() + " for " + self.notes

    def get_total(self): #Extend IntegerField to handle currency?
        return self.total/100.0

    def set_total(self, new_total):
        self.total = int(new_total * 100)


class Receipt(models.Model):
    debtor = models.ForeignKey(User)
    amount = models.IntegerField()
    purchase = models.ForeignKey(Payment)

    def __unicode__(self):
        return (self.debtor.get_full_name() + " owes " + self.get_amount() + " to " + 
                self.purchase.payer.get_full_name())
    
    def get_amount(self): #Extend IntegerField to handle currency?
        return self.amount/100.0

    def set_total(self, new_amount):
        self.amount = int(new_amount * 100)
