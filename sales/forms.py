from django import forms
from .models import Invoice, InvoiceItem, Receipt


class InvoiceForm(forms.ModelForm):
    class Meta:
        model = Invoice
        fields = ['rate', 'balancetype', 'paymenttype', 'balance', 'status', 'customer']


class InvoiceItemForm(forms.ModelForm):
    class Meta:
        model = InvoiceItem
        fields = ['weight', 'touch', 'total', 'is_return', 'quantity', 'product', 'invoice']


class ReceiptForm(forms.ModelForm):
    class Meta:
        model = Receipt
        fields = ['type', 'total', 'description', 'customer']


