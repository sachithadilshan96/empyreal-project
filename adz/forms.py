from django.forms import ModelForm
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
