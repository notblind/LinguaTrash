from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import ApiPartner

urlpatterns = [
    path("", ApiPartner.as_view(), name="partner"),
]
