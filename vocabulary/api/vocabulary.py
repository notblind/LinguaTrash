from rest_framework.generics import (
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView,
)
from rest_framework.permissions import IsAuthenticated

from accounts.models import Partner
from vocabulary.models import Vocabulary
from vocabulary.serializers import (
    FullVocabularySerializer,
    VocabularySerializer,
)


class VocabularyListCreateAPI(ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = FullVocabularySerializer

    def get_queryset(self):
        partner = Partner.objects.get(user_id=self.request.user.id)
        return Vocabulary.objects.filter(partner_id=partner.id)

    def post(self, request, *args, **kwargs):
        partner = Partner.objects.get(user_id=self.request.user.id)
        request.data["partner_id"] = partner.id
        return self.create(request, *args, **kwargs)


class VocabularyAPI(RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = VocabularySerializer

    def get_queryset(self):
        partner = Partner.objects.get(user_id=self.request.user.id)
        return Vocabulary.objects.filter(partner_id=partner.id)
