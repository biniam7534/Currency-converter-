from django import form

from django import forms

CURRENCIES = [
    # A short list to start; expand later or pull dynamically
    ('USD', 'USD'),
    ('EUR', 'EUR'),
    ('GBP', 'GBP'),
    ('JPY', 'JPY'),
    ('ETB', 'ETB'),  
    ('CAD', 'CAD'),
    ('AUD', 'AUD'),
]

class ConvertForm(forms.Form):
    amount = forms.DecimalField(min_value=0, decimal_places=6, max_digits=20, initial=1)
    from_currency = forms.ChoiceField(choices=CURRENCIES)
    to_currency = forms.ChoiceField(choices=CURRENCIES)
