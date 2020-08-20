from django.db import models

from django.contrib.auth.models import User

class Mortgage(models.Model):
    title = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    zipcode = models.CharField(max_length=20)
    maximum_loan_amount = models.IntegerField(default=0)
    interest_rate= models.DecimalField(max_digits=4, decimal_places=1,default=0)
    description = models.TextField(max_length=1000)
    photo_main = models.ImageField(upload_to='photos/%Y/%m/%d/')
    user = models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self):
        return self.title
