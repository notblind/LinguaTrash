from django.urls import path

from .views import ExtraApi, PartnerApi, TrainingApi, VocabularyApi

urlpatterns = [
    path("", VocabularyApi.as_view()),
    path("/partner", PartnerApi.as_view()),
    path("/training", TrainingApi.as_view()),
    path("/extra", ExtraApi.as_view()),
]
