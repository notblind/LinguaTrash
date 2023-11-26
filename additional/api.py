from rest_framework.generics import CreateAPIView, ListAPIView

from additional.models import Holiday
from additional.serializers import FeedBackSerializer, HolidaySerializer


class HolidayApi(ListAPIView):
    serializer_class = HolidaySerializer
    queryset = Holiday.objects.all()


class FeedBackApi(CreateAPIView):
    serializer_class = FeedBackSerializer
