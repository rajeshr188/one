from django.contrib import admin
from django import forms
from .models import License, Loan, Release

class LicenseAdminForm(forms.ModelForm):

    class Meta:
        model = License
        fields = '__all__'


class LicenseAdmin(admin.ModelAdmin):
    form = LicenseAdminForm
    list_display = ['name', 'slug', 'created', 'last_updated', 'type', 'shopname', 'address', 'phonenumber', 'propreitor']
    readonly_fields = ['name', 'slug', 'created', 'last_updated', 'type', 'shopname', 'address', 'phonenumber', 'propreitor']

admin.site.register(License, LicenseAdmin)


class LoanAdminForm(forms.ModelForm):

    class Meta:
        model = Loan
        fields = '__all__'


class LoanAdmin(admin.ModelAdmin):
    form = LoanAdminForm
    list_display = ['loanid', 'slug', 'created', 'last_updated', 'itemtype', 'itemdesc', 'itemweight', 'itemvalue', 'loanamount', 'interestrate', 'interest']
    readonly_fields = ['loanid', 'slug', 'created', 'last_updated', 'itemtype', 'itemdesc', 'itemweight', 'itemvalue', 'loanamount', 'interestrate', 'interest']

admin.site.register(Loan, LoanAdmin)


class ReleaseAdminForm(forms.ModelForm):

    class Meta:
        model = Release
        fields = '__all__'


class ReleaseAdmin(admin.ModelAdmin):
    form = ReleaseAdminForm
    list_display = ['releaseid','loan','customer', 'slug', 'created', 'last_updated', 'interestpaid']
    readonly_fields = ['releaseid','loan','customer', 'slug', 'created', 'last_updated', 'interestpaid']

admin.site.register(Release, ReleaseAdmin)
