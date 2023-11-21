from rest_framework.generics import (
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView,
)
from rest_framework.permissions import IsAuthenticated

from vocabulary.models import Vocabulary
from vocabulary.serializers import (
    FullVocabularySerializer,
    VocabularySerializer,
)


class VocabularyListCreateAPI(ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = FullVocabularySerializer

    def get_queryset(self):
        return Vocabulary.objects.filter(
            create_id=self.request.user.id
        ).prefetch_related("words")


class VocabularyAPI(RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = VocabularySerializer

    def get_queryset(self):
        return Vocabulary.objects.filter(create_id=self.request.user.id)
