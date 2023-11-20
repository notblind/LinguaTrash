from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.generics import ListCreateAPIView
from rest_framework.permissions import IsAuthenticated

from vocabulary.models import Word
from vocabulary.serializers import TranslationSerializer, WordSerializer


class WordListCreateAPI(ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = WordSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ["vocabulary_id"]
    queryset = Word.objects.all().prefetch_related("translations")

    def post(self, request, *args, **kwargs):
        res = self.create(request, *args, **kwargs)
        for translate in request.data.get("translations", []):
            if isinstance(translate, str) and translate.strip():
                translate_data = {"translate": translate, "word_id": res.data.get("id")}
                serializer = TranslationSerializer(data=translate_data)
                if serializer.is_valid(raise_exception=False):
                    serializer.save()
        return res
