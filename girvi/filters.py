from . models import Customer,Loan
import django_filters

class LoanFilter(django_filters.FilterSet):
    class Meta:
        model=Loan
        fields=['loanid','customer','itemtype','license']
