from rest_framework.generics import GenericAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from accounts.models import Partner
from accounts.serializers import PartnerSerializer


class PartnerAPI(GenericAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = PartnerSerializer
    queryset = Partner.objects.all()

    def get(self, request, *args, **kwargs):
        serializer = self.get_serializer(self.get_queryset())
        return Response(serializer.data)

    def get_queryset(self):
        return Partner.objects.get(user_id=self.request.user.id)
