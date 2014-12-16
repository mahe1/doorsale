from django import forms

from doorsale.geo.models import State, Address
from django.utils.translation import ugettext as _

class AddressForm(forms.ModelForm):
    """
    Address form for checkout
    """
    class Meta:
        model = Address
        fields = ('first_name', 'last_name', 'email', 'address1', 'address2',
                  'phone_number', 'fax_number', 'zip_or_postal_code', 'city', 'country', 'state', 'company')
        widgets = {
            'first_name': forms.TextInput(attrs=({'placeholder': _('First name...'), 'class': 'mandatory'})),
            'last_name': forms.TextInput(attrs=({'placeholder': _('Last name...'), 'class': 'mandatory'})),
            'email': forms.TextInput(attrs=({'placeholder': _('Email address...'), 'class': 'mandatory'})),
            'phone_number': forms.TextInput(attrs=({'placeholder': _('Phone number...'), 'class': 'mandatory'})),
            'fax_number': forms.TextInput(attrs=({'placeholder': _('Fax number... (Optional)'), 'class': 'optional'})),
            'address1': forms.TextInput(attrs=({'placeholder': _('Address line 1...'), 'class': 'mandatory'})),
            'address2': forms.TextInput(attrs=({'placeholder': _('Address line 2... (Optional)'), 'class': 'optional'})),
            'zip_or_postal_code': forms.TextInput(attrs=({'placeholder': _('Zip/Postal Code...'), 'class': 'mandatory'})),
            'city': forms.TextInput(attrs=({'placeholder': _('City...'), 'class': 'mandatory'})),
            'Country': forms.Select(attrs=({'placeholder': _('Country...'), 'class': 'mandatory'})),
            'company': forms.TextInput(attrs=({'placeholder': _('Company... (Optional)'), 'class': 'optional'})),

        }
        error_messages = {
            'first_name': {'required': _('Please enter your first name.')},
            'last_name': {'required': _('Please enter your last name.')},
            'email': {'required': _('Please enter your email address.')},
            'address1': {'required': _('Please enter your address.')},
            'city': {'required': _('Please specify your city.')},
            'zip_or_postal_code': {'required': _('Please enter Zip or Postal Code.')},
            'country': {'required': _('Please specify your country.')},
            'phone_number': {'required': _('Please entery your phone number.')}
        }

    def __init__(self, *args, **kwargs):
        super(AddressForm, self).__init__(*args, **kwargs)
        self.fields['country'].empty_label = None

    @classmethod
    def get_states(cls):
        return list(State.objects.filter(is_active=True).all())
