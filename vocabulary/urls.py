from django.urls import path

from vocabulary.api import (
    VocabularyAPI,
    VocabularyListCreateAPI,
    WordListCreateAPI,
)
from vocabulary.views import ExtraApi, PartnerApi, TrainingApi, VocabularyApi

urlpatterns = [
    path("", VocabularyApi.as_view()),
    path("api/v1/vocabulary", VocabularyListCreateAPI.as_view()),
    path("api/v1/vocabulary/<int:pk>", VocabularyAPI.as_view()),
    path("api/v1/word", WordListCreateAPI.as_view()),
    path("/partner", PartnerApi.as_view()),
    path("/training", TrainingApi.as_view()),
    path("/extra", ExtraApi.as_view()),
]
