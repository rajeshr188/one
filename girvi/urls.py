from django.urls import path, include
from rest_framework import routers

from . import api
from . import views

router = routers.DefaultRouter()
router.register(r'license', api.LicenseViewSet)
router.register(r'loan', api.LoanViewSet)
router.register(r'release', api.ReleaseViewSet)


urlpatterns = (
    # urls for Django Rest Framework API
    path('api/v1/', include(router.urls)),
)

urlpatterns += (
    # urls for License
    path('girvi/license/', views.LicenseListView.as_view(), name='girvi_license_list'),
    path('girvi/license/create/', views.LicenseCreateView.as_view(), name='girvi_license_create'),
    path('girvi/license/detail/<slug:slug>/', views.LicenseDetailView.as_view(), name='girvi_license_detail'),
    path('girvi/license/update/<slug:slug>/', views.LicenseUpdateView.as_view(), name='girvi_license_update'),
)

urlpatterns += (
    # urls for Loan
    path('girvi/loan/', views.LoanListView.as_view(), name='girvi_loan_list'),
    path('girvi/loan/create/', views.LoanCreateView.as_view(), name='girvi_loan_create'),
    path('girvi/loan/detail/<slug:slug>/', views.LoanDetailView.as_view(), name='girvi_loan_detail'),
    path('girvi/loan/update/<slug:slug>/', views.LoanUpdateView.as_view(), name='girvi_loan_update'),
)

urlpatterns += (
    # urls for Release
    path('girvi/release/', views.ReleaseListView.as_view(), name='girvi_release_list'),
    path('girvi/release/create/', views.ReleaseCreateView.as_view(), name='girvi_release_create'),
    path('girvi/release/detail/<slug:slug>/', views.ReleaseDetailView.as_view(), name='girvi_release_detail'),
    path('girvi/release/update/<slug:slug>/', views.ReleaseUpdateView.as_view(), name='girvi_release_update'),
)

