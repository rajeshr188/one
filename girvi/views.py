from django.views.generic import DetailView, ListView, UpdateView, CreateView
from .models import License, Loan, Release
from .forms import LicenseForm, LoanForm, ReleaseForm


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


class LoanListView(ListView):
    model = Loan


class LoanCreateView(CreateView):
    model = Loan
    form_class = LoanForm


class LoanDetailView(DetailView):
    model = Loan


class LoanUpdateView(UpdateView):
    model = Loan
    form_class = LoanForm


class ReleaseListView(ListView):
    model = Release


class ReleaseCreateView(CreateView):
    model = Release
    form_class = ReleaseForm


class ReleaseDetailView(DetailView):
    model = Release


class ReleaseUpdateView(UpdateView):
    model = Release
    form_class = ReleaseForm

