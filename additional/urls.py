from django.urls import path

from additional.api import FeedBackApi, HolidayApi

urlpatterns = [
    path("feedback", FeedBackApi.as_view()),
    path("holiday", HolidayApi.as_view()),
]
