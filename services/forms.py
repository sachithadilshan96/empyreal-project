from django.forms import ModelForm
from django import forms
from.models import Mortgage,Legal,Builder
from osm_field.fields import LatitudeField, LongitudeField, OSMField

class MortgageForm(ModelForm):
        class Meta:
            model = Mortgage
            fields = [  'title',
                        'company',
                        'address',
                        'city',
                        'state',
                        'zipcode',
                        'maximum_loan_amount',
                        'interest_rate',
                        'description',
                        'contact_number',
                        'photo_main',
                        'Email']

class LegalForm(ModelForm):
        class Meta:
            model = Legal
            fields = [  'title',
                        'law_firm_name',
                        'address',
                        'city',
                        'state',
                        'zipcode',
                        'hourly_rate',
                        'description',
                        'contact_number',
                        'photo_main',
                        'Email']


class  BuilderForm(ModelForm):
        class Meta:
            model =  Builder
            fields = [  'title',
                        'company_name',
                        'service_in_brief',
                        'address',
                        'city',
                        'state',
                        'zipcode',
                        'description',
                        'contact_number',
                        'photo_main',
                        'photo_1',
                        'photo_2',
                        'photo_3',
                        'photo_4',
                        'photo_5',
                        'photo_6',
                        'Email']


Waterfront_Choices= [
    (0, 'No'),
    (1, 'Yes'),
    ]

View_Choices= [tuple([x,x]) for x in range(0,5)]


Condition_Choices= [tuple([x,x]) for x in range(1,6)]

Grade_Choices= [tuple([x,x]) for x in range(1,14)]

class PredictForm(forms.Form):
    bedrooms = forms.IntegerField(label='No of bedrooms')
    bathrooms = forms.IntegerField(label='No of bathrooms')
    sqft_living = forms.IntegerField(label='Sqft of living area')
    sqft_lot = forms.IntegerField(label='Sqft of lot area')
    floors = forms.IntegerField(label='Floors')
    waterfront = forms.IntegerField(label='Waterfront or not',widget=forms.Select(choices=Waterfront_Choices))
    view = forms.IntegerField(label='Rate the outside view from the house',widget=forms.Select(choices=View_Choices))
    condition = forms.IntegerField(label='Rate the construction condition',widget=forms.Select(choices=Condition_Choices))
    grade = forms.IntegerField(label='Rate building design',widget=forms.Select(choices=Grade_Choices))
    sqft_above = forms.IntegerField(label='Sqft above ground level')
    sqft_basement = forms.IntegerField(label='Sqft of the basement')
    yr_built = forms.IntegerField(label='Year built')
    yr_renovated = forms.IntegerField(label='Year renovated')
    zipcode = forms.IntegerField(label='Zipcode')
    location_lat = forms.FloatField(label='Add location latitude')
    location_lon = forms.FloatField(label='Add location longitude')
    sqft_living15 = forms.IntegerField(label='Sqft of neighbouring house')
    sqft_lot15 = forms.IntegerField(label='Lot sqft of neighbouring house')
