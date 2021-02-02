from django.urls import path
from .views import VocabularyApi, PartnerApi

urlpatterns = [
	path('', VocabularyApi.as_view()),
	path('/partner', PartnerApi.as_view())
]
