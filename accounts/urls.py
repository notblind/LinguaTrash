from django.urls import include, path

from accounts.api import PartnerAPI

urlpatterns = [
    path("api/v1/partner", PartnerAPI.as_view(), name="partner"),
]
