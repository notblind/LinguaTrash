from rest_framework.generics import (
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView,
)
from rest_framework.permissions import IsAuthenticated

from accounts.models import Partner
from accounts.serializers import PartnerSerializer
from vocabulary.models import DayOfWeek, Holiday, Vocabulary, Words
from vocabulary.serializers import (
    FeedBackSerializer,
    FullVocabularySerializer,
    HolidaySerializer,
    TranslationSerializer,
    VocabularySerializer,
    WordSerializer,
    WordSerializerForSecondMode,
    WordSerializerForThirdMode,
)


class VocabularyListCreateAPI(ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = FullVocabularySerializer

    def get_queryset(self):
        partner = Partner.objects.get(user=self.request.user.id)
        return Vocabulary.objects.filter(partner=partner.id)

    def post(self, request, *args, **kwargs):
        partner = Partner.objects.get(user=self.request.user.id)
        request.data["partner"] = partner.id
        return self.create(request, *args, **kwargs)


class VocabularyAPI(RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = VocabularySerializer

    def get_queryset(self):
        partner = Partner.objects.get(user=self.request.user.id)
        return Vocabulary.objects.filter(partner=partner.id)


class WordListCreateAPI(ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = WordSerializer

    def get_queryset(self):
        return Words.objects.filter(vocabulary=self.request.data.get("idVocabulary"))
