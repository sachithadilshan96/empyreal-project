from django.forms import ModelForm
from.models import UserProfile
#UserProfile form
class UserProfileForm(ModelForm):
        class Meta:
            model = UserProfile
            fields = [  'profile_picture',
                        'address',
                        'city',
                        'state',
                        'zipcode',
                        'bio',
                        'contact_number',
                        ]
