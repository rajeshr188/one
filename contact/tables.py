import django_tables2 as tables
from django_tables2.utils import A
from .models import Customer

from django.utils.html import format_html

class ImageColumn(tables.Column):
    def render(self, value):
        return format_html('<img src="{}" width="50" height="50" class="img-fluid img-thumbnail" alt={}/>', value.url,value.name)
class CustomerTable(tables.Table):
    name = tables.LinkColumn('contact_customer_detail', args=[A('slug')])
    pic = ImageColumn()
    relatedas=tables.Column(orderable=False)
    edit = tables.LinkColumn('contact_customer_update', args=[A('slug')],attrs={'a':{"class":"btn btn-outline-info","role":"button"}}, orderable=False, empty_values=())
    delete = tables.LinkColumn('contact_customer_delete', args=[A('slug')],attrs={'a':{"class":"btn btn-outline-danger","role":"button"}}, orderable=False, empty_values=())
    
    def render_edit(self):
        return 'Edit'
    def render_delete(self):
        return 'Delete'
    class Meta:
        model = Customer
        fields = ('pic','id','name', 'relatedto',
                'relatedas', 'address', 'area','phonenumber',
                    )
        attrs = {"class": "table table-striped table-bordered"}
        empty_text = "There are no customers matching the search criteria..."
        # template_name = 'django_tables2/bootstrap.html'
