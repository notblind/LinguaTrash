from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.generics import (
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView,
)
from rest_framework.permissions import IsAuthenticated

from accounts.models import Partner
from accounts.serializers import PartnerSerializer
from vocabulary.models import (
    DayOfWeek,
    Holiday,
    Translation,
    Vocabulary,
    Words,
)
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
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ["vocabulary"]

    def get_queryset(self):
        return Words.objects.all()

    def post(self, request, *args, **kwargs):
        res = self.create(request, *args, **kwargs)
        for translate in request.data.get("translations", []):
            if isinstance(translate, str) and translate.strip():
                translate_data = {"translate": translate, "word": res.data.get("id")}
                serializer = TranslationSerializer(data=translate_data)
                if serializer.is_valid(raise_exception=False):
                    serializer.save()
        return res
