from django.views.generic import DetailView, ListView, UpdateView, CreateView,DeleteView
from .models import Customer, Supplier
from .forms import CustomerForm, SupplierForm
from django.urls import reverse,reverse_lazy
from girvi.models import Loan
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

class CustomerDelete(DeleteView):
    model=Customer
    success_url = reverse_lazy('contact_customer_list')

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

class SupplierDelete(DeleteView):
    model=Supplier
    success_url = reverse_lazy('contact_supplier_list')
