from django.views.generic import DetailView, ListView, UpdateView, CreateView,DeleteView
from .models import License, Loan, Release
from .forms import LicenseForm, LoanForm, ReleaseForm
from django.urls import reverse,reverse_lazy
from contact.models import Customer
from django_tables2 import RequestConfig
from django_tables2.views import SingleTableMixin
from django_tables2.export.views import ExportMixin
from .tables import LoanTable
from django_filters.views import FilterView
from .filters import LoanFilter
import re
class LicenseListView(ListView):
    model = License

class LicenseCreateView(CreateView):
    model = License
    form_class = LicenseForm

class LicenseDetailView(DetailView):
    model = License

class LicenseUpdateView(UpdateView):
    model = License
    form_class = LicenseForm

class LicenseDeleteView(DeleteView):
    model=License
    success_url=reverse_lazy('girvi_license_list')

class LoanListView(ExportMixin,SingleTableMixin,FilterView):
    table_class=LoanTable
    # table_data=Loan.objects.all()
    model = Loan
    template_name='girvi/loan_list.html'
    filterset_class=LoanFilter
    paginate_by=50

def incloanid():
    last=Loan.objects.all().order_by('id').last()
    if not last:
        return '1'
    splitl=re.split('(\d+)',last.loanid)
    billno=splitl[0] + str(int(splitl[1])+1)
    return str(billno)

def ld():
    last=Loan.objects.all().order_by('id').last()
    if not last:
        return '1'
    return last.created

class LoanCreateView(CreateView):
    model = Loan
    form_class = LoanForm

    def get_initial(self):
        if self.kwargs:
            customer=Customer.objects.get(id=self.kwargs['pk'])
            # license=License.objects.get(id=2)
            return{
                'customer':customer,
                'loanid':incloanid,
                # 'license':license,
                'created':ld,
            }

class LoanDetailView(DetailView):
    model = Loan

class LoanUpdateView(UpdateView):
    model = Loan
    form_class = LoanForm

class LoanDeleteView(DeleteView):
    model=Loan
    success_url=reverse_lazy('girvi_loan_list')

class ReleaseListView(ListView):
    model = Release

class ReleaseCreateView(CreateView):
    model = Release
    form_class = ReleaseForm

    def get_initial(self):
        if self.kwargs:
            loan=Loan.objects.get(slug=self.kwargs['slug'])
            return{'loan':loan,'interestpaid':loan.interestdue,}

class ReleaseDetailView(DetailView):
    model = Release

class ReleaseUpdateView(UpdateView):
    model = Release
    form_class = ReleaseForm

class ReleaseDeleteView(DeleteView):
    model=Release
    success_url=reverse_lazy('girvi_release_list')
