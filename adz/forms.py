#importing model froms
from django.forms import ModelForm
#Listing model import 
from listings.models import Listing
class AdzForm(ModelForm):
        class Meta:
            model = Listing
            fields =    ['realtor',
                        'title',
                        'address',
                        'city',
                        'state',
                        'zipcode',
                        'description',
                        'price',
                        'bedrooms',
                        'bathrooms',
                        'garage',
                        'sqft',
                        'lot_size',
                        'sqft_living',
                        'floors',
                        'waterfront',
                        'view',
                        'condition',
                        'grade',
                        'sqft_above',
                        'sqft_basement',
                        'yr_built',
                        'yr_renovated',
                        'sqft_living15',
                        'sqft_lot15',
                        'photo_main',
                        'photo_1',
                        'photo_2',
                        'photo_3',
                        'photo_4',
                        'photo_5',
                        'photo_6',
                        'location',
                        'location_lat',
                        'location_lon',

                        ]
