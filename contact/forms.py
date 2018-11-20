from django import forms
from .models import Customer, Supplier


class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ['name', 'phonenumber', 'Address', 'type', 'relatedas', 'relatedto']


class SupplierForm(forms.ModelForm):
    class Meta:
        model = Supplier
        fields = ['name', 'organisation', 'phonenumber', 'initial']
