from datetime import date

from django.db import models

# Create your models here.
class Details(models.Model):
 billno = models.IntegerField()
 bname = models.CharField(max_length=20)
 baddress =models.CharField(max_length=200)
 bphonenumber =models.IntegerField()
 sname =models.CharField(max_length=30)
 saddress =models.TextField()
 sphonenumber =models.IntegerField()


class Bill(models.Model):
 billno = models.IntegerField()
 slno =models.IntegerField()
 product =models.CharField(max_length=10)
 quantity =models.IntegerField()
 price =models.IntegerField()
 total = models.IntegerField()
