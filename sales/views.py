from django.views.generic import DetailView, ListView, UpdateView, CreateView
from .models import Invoice, InvoiceItem, Receipt
from .forms import InvoiceForm, InvoiceItemForm, ReceiptForm


class InvoiceListView(ListView):
    model = Invoice


class InvoiceCreateView(CreateView):
    model = Invoice
    form_class = InvoiceForm


class InvoiceDetailView(DetailView):
    model = Invoice


class InvoiceUpdateView(UpdateView):
    model = Invoice
    form_class = InvoiceForm


class InvoiceItemListView(ListView):
    model = InvoiceItem


class InvoiceItemCreateView(CreateView):
    model = InvoiceItem
    form_class = InvoiceItemForm


class InvoiceItemDetailView(DetailView):
    model = InvoiceItem


class InvoiceItemUpdateView(UpdateView):
    model = InvoiceItem
    form_class = InvoiceItemForm


class ReceiptListView(ListView):
    model = Receipt


class ReceiptCreateView(CreateView):
    model = Receipt
    form_class = ReceiptForm


class ReceiptDetailView(DetailView):
    model = Receipt


class ReceiptUpdateView(UpdateView):
    model = Receipt
    form_class = ReceiptForm

