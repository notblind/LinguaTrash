import random

from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.generics import GenericAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from vocabulary.mixins import FilterQByCreatedMixin
from vocabulary.models import Word
from vocabulary.serializers import (
    WordSerializer,
    WordSerializerForSecondMode,
    WordSerializerForThirdMode,
)


class TrainingCardApi(FilterQByCreatedMixin, GenericAPIView):
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ["vocabulary_id"]
    queryset = Word.objects.all().prefetch_related("translations")

    def get_serializer_class(self):
        mode = self.request.query_params.get("mode")
        if mode == "translation":
            return WordSerializerForSecondMode
        elif mode == "reverse_translation":
            return WordSerializerForThirdMode
        return WordSerializer

    def get(self, request, *args, **kwargs):
        words = sorted(
            self.filter_queryset(self.get_queryset()), key=lambda x: random.random()
        )
        serializer = self.get_serializer(words, many=True)
        return Response(serializer.data)
