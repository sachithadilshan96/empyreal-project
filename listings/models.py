#models importing
from django.db import models
from datetime import datetime
from realtors.models import Realtor
from django.contrib.auth.models import User

#Using LongitudeField and LatitudeField
from osm_field.fields import LatitudeField, LongitudeField, OSMField

#User choices defining
Waterfront_Choices= [
    (0, 'No'),
    (1, 'Yes'),
    ]

View_Choices= [tuple([x,x]) for x in range(0,5)]


Condition_Choices= [tuple([x,x]) for x in range(1,6)]

Grade_Choices= [tuple([x,x]) for x in range(1,14)]

#Listing Model
class Listing(models.Model):
  user = models.ForeignKey(User,on_delete=models.DO_NOTHING,default=2)
  realtor = models.ForeignKey(Realtor, on_delete=models.DO_NOTHING)
  title = models.CharField(max_length=200)
  address = models.CharField(max_length=200)
  city = models.CharField(max_length=100)
  state = models.CharField(max_length=100)
  zipcode = models.CharField(max_length=20)
  description = models.TextField(blank=True)
  price = models.IntegerField()
  bedrooms = models.IntegerField()
  bathrooms = models.DecimalField(max_digits=2, decimal_places=1)
  garage = models.IntegerField()
  sqft = models.IntegerField()
  sqft_living = models.IntegerField()
  lot_size = models.DecimalField(max_digits=5, decimal_places=1)
  floors = models.IntegerField()
  waterfront = models.IntegerField(choices=Waterfront_Choices)
  view = models.IntegerField(choices=View_Choices)
  condition = models.IntegerField(choices=Condition_Choices)
  grade = models.IntegerField(choices=Grade_Choices)
  sqft_above = models.IntegerField()
  sqft_basement = models.IntegerField()
  yr_built = models.IntegerField()
  yr_renovated = models.IntegerField()
  sqft_living15 = models.IntegerField()
  sqft_lot15 = models.IntegerField()
  photo_main = models.ImageField(upload_to='photos/%Y/%m/%d/')
  photo_1 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
  photo_2 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
  photo_3 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
  photo_4 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
  photo_5 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
  photo_6 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
  is_published = models.BooleanField(default=True)
  is_verified = models.BooleanField(default=False)
  list_date = models.DateTimeField(default=datetime.now, blank=True)
  likes = models.ManyToManyField(User,related_name='adz_posts')
  location = OSMField()
  location_lat = LatitudeField()
  location_lon = LongitudeField()

  def total_likes(self):
      return self.likes.count()

  def __str__(self):
    return self.title
