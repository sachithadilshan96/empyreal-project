from django.db import models
#importing django user default authenticaton
from django.contrib.auth.models import User
#extending to user profile

class UserProfile(models.Model):
    user = models.OneToOneField(User,primary_key=True,on_delete=models.CASCADE)
    profile_picture = models.ImageField(upload_to='photos/%Y/%m/%d/',default="media\photos\2020\08\30\images.png")
    address = models.CharField(max_length=200,blank=True)
    city = models.CharField(max_length=100,blank=True)
    state = models.CharField(max_length=100,blank=True)
    zipcode = models.CharField(max_length=20,blank=True)
    bio = models.TextField(max_length=1000,blank=True)
    contact_number = models.IntegerField(blank=True,null=True)


    def __str__(self):
        return self.user.username
