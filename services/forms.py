from django.forms import ModelForm
from.models import Mortgage,Legal,Builder

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
