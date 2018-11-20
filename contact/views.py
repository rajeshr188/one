from django.views.generic import DetailView, ListView, UpdateView, CreateView,DeleteView
from django_tables2 import RequestConfig
from django_tables2.views import SingleTableMixin
from django_tables2.export.views import ExportMixin
from .tables import CustomerTable
from django_filters.views import FilterView
from .filters import CustomerFilter
from .models import Customer, Supplier
from .forms import CustomerForm, SupplierForm
from django.urls import reverse,reverse_lazy
from girvi.models import Loan

class CustomerListView(ExportMixin,SingleTableMixin,FilterView):
    table_class = CustomerTable
    # table_data = Customer.objects.all()
    # paginator_class = LazyPaginator
    model = Customer
    template_name = 'contact/customer_list.html'
    filterset_class = CustomerFilter
    paginate_by = 50

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
