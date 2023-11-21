from django.urls import path

from accounts.api import UserAPI

urlpatterns = [
    path("api/v1/user", UserAPI.as_view(), name="api_user"),
]
