from django.views.generic import DetailView, ListView, UpdateView, CreateView
from .models import Customer, Supplier
from .forms import CustomerForm, SupplierForm


class CustomerListView(ListView):
    model = Customer


class CustomerCreateView(CreateView):
    model = Customer
    form_class = CustomerForm


class CustomerDetailView(DetailView):
    model = Customer


class CustomerUpdateView(UpdateView):
    model = Customer
    form_class = CustomerForm


class SupplierListView(ListView):
    model = Supplier


class SupplierCreateView(CreateView):
    model = Supplier
    form_class = SupplierForm


class SupplierDetailView(DetailView):
    model = Supplier


class SupplierUpdateView(UpdateView):
    model = Supplier
    form_class = SupplierForm

