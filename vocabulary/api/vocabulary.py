from rest_framework.generics import (
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView,
)
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from vocabulary.mixins import FilterQByCreatedMixin
from vocabulary.models import Vocabulary
from vocabulary.serializers import (
    FullVocabularySerializer,
    VocabularySerializer,
)


class VocabularyListCreateAPI(FilterQByCreatedMixin, ListCreateAPIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = FullVocabularySerializer
    queryset = Vocabulary.objects.all().prefetch_related("words")


class VocabularyAPI(FilterQByCreatedMixin, RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = VocabularySerializer
    queryset = Vocabulary.objects.all()
