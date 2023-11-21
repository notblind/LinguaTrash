from rest_framework.generics import CreateAPIView, ListAPIView
from rest_framework.permissions import IsAuthenticated

from additional.models import Holiday
from additional.serializers import FeedBackSerializer, HolidaySerializer


class HolidayApi(ListAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = HolidaySerializer
    queryset = Holiday.objects.all()


class FeedBackApi(CreateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = FeedBackSerializer
