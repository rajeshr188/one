from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/', include('django.contrib.auth.urls')),
    path('accounts/', include('allauth.urls')),
    path('', include('pages.urls')),
    path('contact/',include('contact.urls')),
    path('product/',include('product.urls')),
    path('girvi/',include('girvi.urls')),
    path('chitfund',include('Chitfund.urls')),
    path('select2/', include('django_select2.urls')),
]
