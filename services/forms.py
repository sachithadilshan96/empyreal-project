from django.forms import ModelForm
from.models import Mortgage
class MortgageForm(ModelForm):
        class Meta:
            model = Mortgage
            fields = [  'title',
                        'address',
                        'city',
                        'state',
                        'zipcode',
                        'maximum_loan_amount',
                        'interest_rate',
                        'description',
                        'photo_main']
