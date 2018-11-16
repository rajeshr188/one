from django import forms
from .models import License, Loan, Release


class LicenseForm(forms.ModelForm):
    class Meta:
        model = License
        fields = ['name', 'type', 'shopname', 'address', 'phonenumber', 'propreitor']


class LoanForm(forms.ModelForm):
    class Meta:
        model = Loan
        fields = ['loanid', 'itemtype', 'itemdesc', 'itemweight', 'itemvalue', 'loanamount', 'interestrate', 'interest', 'license', 'customer']


class ReleaseForm(forms.ModelForm):
    class Meta:
        model = Release
        fields = ['releaseid', 'interestpaid', 'loan']


