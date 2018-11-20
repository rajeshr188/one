import django_tables2 as tables
from django_tables2.utils import A
from .models import Customer


class CustomerTable(tables.Table):
  name = tables.LinkColumn('contact_customer_detail', args=[A('slug')])
  
  # update=tables.LinkColumn('contact_customer_update',args=[A('slug')])
  # customer_first_name = tables.LinkColumn('customer-detail', args=[A('pk')])
  # customer_last_name = tables.LinkColumn('customer-detail', args=[A('pk')])
  # customer_email = tables.LinkColumn('customer-detail', args=[A('pk')])

  class Meta:
    model = Customer
    fields = ('id','name', 'relatedto',
              'relatedas', 'address', 'area','phonenumber',
              )
    attrs = {"class": "table table-striped table-bordered"}
    empty_text = "There are no customers matching the search criteria..."
    # template_name = 'django_tables2/bootstrap.html'
