from rest_framework.generics import CreateAPIView, ListAPIView
from rest_framework.permissions import IsAuthenticated

from accounts.models import Partner
from additional.models import Holiday
from additional.serializers import FeedBackSerializer, HolidaySerializer


class HolidayApi(ListAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = HolidaySerializer
    queryset = Holiday.objects.all()


class FeedBackApi(CreateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = FeedBackSerializer

    def post(self, request, *args, **kwargs):
        partner = Partner.objects.get(user_id=self.request.user.id)
        request.data["partner_id"] = partner.id
        return self.create(request, *args, **kwargs)
