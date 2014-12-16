from django import forms

from doorsale.catalog.models import Manufacturer, Category
from django.utils.translation import ugettext as _

class AdvancedSearchForm(forms.Form):
    """
    Advanced Catalog Search form
    """
    keyword = forms.CharField(max_length=15, error_messages={'required': _('Please enter search keyword.')},
                              widget=forms.TextInput(attrs={'placeholder': _('Search store...')}))
    category = forms.ModelChoiceField(required=False, queryset=Category.objects.filter(
        is_active=True), empty_label=_('all...'))
    manufacturer = forms.ModelChoiceField(
        required=False, queryset=Manufacturer.objects.filter(is_active=True), empty_label=_('all...'))
    price_from = forms.IntegerField(
        required=False, label=_('Price From'), widget=forms.TextInput(attrs={'placeholder': _('From...')}))
    price_to = forms.IntegerField(
        required=False, label=_('Price To'), widget=forms.TextInput(attrs={'placeholder': _('To...')}))

    def clean_price_to(self):
        price_from = self.cleaned_data.get('price_from', None)
        price_to = self.cleaned_data.get('price_to', None)

        if price_from and price_to and int(price_from) > int(price_to):
            raise forms.ValidationError(_("Please provide a valid price range."))

        return price_to