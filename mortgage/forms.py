from django import forms

class loan_inputForm(forms.Form):
    amount = forms.FloatField(Label='Loan amount')
    year = forms.IntegerField(Label='Year')
    month = forms.IntegerField(Label = 'month')
    rate = forms.IntegerField(Label = 'rate')