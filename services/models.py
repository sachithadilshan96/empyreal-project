from django.db import models
from datetime import datetime
from django.contrib.auth.models import User



class Mortgage(models.Model):
    title = models.CharField(max_length=200)
    company = models.CharField(max_length=200,default='')
    address = models.CharField(max_length=200)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    zipcode = models.CharField(max_length=20)
    maximum_loan_amount = models.IntegerField(default=0)
    interest_rate= models.DecimalField(max_digits=4, decimal_places=1,default=0)
    description = models.TextField(max_length=1000)
    contact_number = models.IntegerField()
    photo_main = models.ImageField(upload_to='photos/%Y/%m/%d/')
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    Email = models.EmailField(max_length=254, default='')
    is_verified = models.BooleanField(default=False)
    list_date = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return self.title

class Legal(models.Model):
    title = models.CharField(max_length=200)
    law_firm_name = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    zipcode = models.CharField(max_length=20)
    hourly_rate = models.IntegerField(default=0)
    description = models.TextField(max_length=1000)
    contact_number = models.IntegerField()
    photo_main = models.ImageField(upload_to='photos/%Y/%m/%d/')
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    Email = models.EmailField(max_length=254, default='')
    is_verified = models.BooleanField(default=False)
    list_date = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return self.title



class Builder(models.Model):
    title = models.CharField(max_length=200)
    company_name = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    zipcode = models.CharField(max_length=20)
    service_in_brief = models.CharField(max_length=30)
    description = models.TextField(max_length=1000)
    contact_number = models.IntegerField()
    photo_main = models.ImageField(upload_to='photos/%Y/%m/%d/')
    photo_1 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_2 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_3 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_4 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_5 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_6 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    Email = models.EmailField(max_length=254, default='')
    is_verified = models.BooleanField(default=False)
    list_date = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return self.title
