from __future__ import unicode_literals
from django.db import models

# Create your models here.



class bank_table(models.Model):
    bank_ac_num=models.IntegerField(primary_key=True)
    bank_ifci_code=models.CharField(max_length=30)
    user_status=models.BooleanField(default=True)
    def __unicode__(self):
        return "%s"%self.bank_ac_num

class wallet_table(models.Model):
    mob_num=models.IntegerField(primary_key=True)
    bank_ac_num=models.OneToOneField(bank_table,on_delete=models.CASCADE)
    wallet_amnt=models.IntegerField(default=0)
    def __unicode__(self):
        return "%s"%self.mob_num

class user_table(models.Model):
    user_id=models.AutoField(primary_key=True)
    user_name=models.CharField(max_length=30)
    mob_num=models.OneToOneField(wallet_table,null=False)
    def __unicode__(self):
        return "%s"%self.user_id
