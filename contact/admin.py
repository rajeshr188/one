from django.contrib import admin
from django import forms
from .models import Customer, Supplier

class CustomerAdminForm(forms.ModelForm):

    class Meta:
        model = Customer
        fields = '__all__'


class CustomerAdmin(admin.ModelAdmin):
    form = CustomerAdminForm
    list_display = ['name', 'slug', 'created', 'last_updated', 'phonenumber', 'Address', 'type', 'relatedas', 'relatedto']
    readonly_fields = ['name', 'slug', 'created', 'last_updated', 'phonenumber', 'Address', 'type', 'relatedas', 'relatedto']

admin.site.register(Customer, CustomerAdmin)


class SupplierAdminForm(forms.ModelForm):

    class Meta:
        model = Supplier
        fields = '__all__'


class SupplierAdmin(admin.ModelAdmin):
    form = SupplierAdminForm
    list_display = ['name', 'slug', 'created', 'last_updated', 'organisation', 'phonenumber', 'initial']
    readonly_fields = ['name', 'slug', 'created', 'last_updated', 'organisation', 'phonenumber', 'initial']

admin.site.register(Supplier, SupplierAdmin)


