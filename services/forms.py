from django.forms import ModelForm
from.models import Mortgage,Legal

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
