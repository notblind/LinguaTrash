from django.urls import path

from vocabulary.api.training import TrainingCardApi
from vocabulary.api.vocabulary import VocabularyAPI, VocabularyListCreateAPI
from vocabulary.api.word import WordListCreateAPI
from vocabulary.views import ExtraApi

urlpatterns = [
    path("api/v1/vocabulary", VocabularyListCreateAPI.as_view()),
    path("api/v1/vocabulary/<int:pk>", VocabularyAPI.as_view()),
    path("api/v1/word", WordListCreateAPI.as_view()),
    path("api/v1/training", TrainingCardApi.as_view()),
    path("/extra", ExtraApi.as_view()),
]
