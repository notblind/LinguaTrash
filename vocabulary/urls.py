from django.urls import path

from vocabulary.api.training import TrainingCardApi
from vocabulary.api.vocabulary import VocabularyAPI, VocabularyListCreateAPI
from vocabulary.api.word import WordListCreateAPI

urlpatterns = [
    path("vocabulary", VocabularyListCreateAPI.as_view()),
    path("vocabulary/<int:pk>", VocabularyAPI.as_view()),
    path("word", WordListCreateAPI.as_view()),
    path("training", TrainingCardApi.as_view()),
]
