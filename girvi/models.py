from django.urls import reverse
from django_extensions.db.fields import AutoSlugField
from django.db.models import CharField
from django.db.models import DateTimeField
from django.db.models import DecimalField
from django.db.models import IntegerField
from django.db.models import PositiveIntegerField
from django.db.models import PositiveSmallIntegerField
from django.db.models import TextField
from django_extensions.db.fields import AutoSlugField
from django.conf import settings
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.contrib.auth import get_user_model
from django.contrib.auth import models as auth_models
from django.db import models as models
from django_extensions.db import fields as extension_fields
from contact.models import Customer

class License(models.Model):

    # Fields
    name = models.CharField(max_length=255)
    slug = extension_fields.AutoSlugField(populate_from='name', blank=True)
    created = models.DateTimeField(auto_now_add=True, editable=False)
    last_updated = models.DateTimeField(auto_now=True, editable=False)
    type = models.CharField(max_length=30)
    shopname = models.CharField(max_length=30)
    address = models.TextField(max_length=100)
    phonenumber = models.CharField(max_length=30)
    propreitor = models.CharField(max_length=30)


    class Meta:
        ordering = ('-created',)

    def __unicode__(self):
        return u'%s' % self.slug

    def get_absolute_url(self):
        return reverse('girvi_license_detail', args=(self.slug,))


    def get_update_url(self):
        return reverse('girvi_license_update', args=(self.slug,))


class Loan(models.Model):

    # Fields
    loanid = models.CharField(max_length=255)
    slug = extension_fields.AutoSlugField(populate_from='loanid', blank=True)
    created = models.DateTimeField(auto_now_add=True, editable=False)
    last_updated = models.DateTimeField(auto_now=True, editable=False)
    itemtype = models.CharField(max_length=30)
    itemdesc = models.TextField(max_length=30)
    itemweight = models.DecimalField(max_digits=10, decimal_places=2)
    itemvalue = models.DecimalField(max_digits=10, decimal_places=2)
    loanamount = models.PositiveIntegerField()
    interestrate = models.PositiveSmallIntegerField()
    interest = models.PositiveIntegerField()

    # Relationship Fields
    license = models.ForeignKey(
        License,
        on_delete=models.CASCADE, related_name="license"
    )
    customer = models.ForeignKey(
        Customer,
        on_delete=models.CASCADE, related_name="investee"
    )

    class Meta:
        ordering = ('-created',)

    def __unicode__(self):
        return u'%s' % self.slug

    def get_absolute_url(self):
        return reverse('girvi_loan_detail', args=(self.slug,))


    def get_update_url(self):
        return reverse('girvi_loan_update', args=(self.slug,))


class Release(models.Model):

    # Fields
    releaseid = models.CharField(max_length=255)
    slug = extension_fields.AutoSlugField(populate_from='releaseid', blank=True)
    created = models.DateTimeField(auto_now_add=True, editable=False)
    last_updated = models.DateTimeField(auto_now=True, editable=False)
    interestpaid = models.IntegerField()

    # Relationship Fields
    loan = models.ForeignKey(
        'girvi.Loan',
        on_delete=models.CASCADE, related_name="loans"
    )
    customer = models.ForeignKey(
        Customer,
        on_delete=models.CASCADE, related_name="releasedby"
    )

    class Meta:
        ordering = ('-created',)

    def __unicode__(self):
        return u'%s' % self.slug

    def get_absolute_url(self):
        return reverse('girvi_release_detail', args=(self.slug,))


    def get_update_url(self):
        return reverse('girvi_release_update', args=(self.slug,))
