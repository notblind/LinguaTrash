import random
from datetime import datetime

from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from accounts.models import Partner

from .models import DayOfWeek, Holiday
from .serializers import FeedBackSerializer, HolidaySerializer


class ExtraApi(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        method = request.data.get("method")

        if method == "create_feedback":
            return self.create_feedback(request)
        elif method == "get_holidays":
            return self.get_holidays(request)

        return Response({"Not allow method"})

    def create_feedback(self, request):
        data = request.data.get("data")
        user = request.user
        if user:
            partner = Partner.objects.get(user=user.id)
            data["partner"] = partner.id
            serializer = FeedBackSerializer(data=data)

            if serializer.is_valid(raise_exception=True):
                res = serializer.save()
                return Response(
                    {"success": "Message created successfully", "status": "success"}
                )

    def get_holidays(self, request):
        now = datetime.now().strftime("%d.%m")
        day_of_week = DayOfWeek.objects.filter(day_text=now)
        data = None
        if len(day_of_week) > 0:
            holidays = Holiday.objects.filter(day=day_of_week[0])
            data = HolidaySerializer(holidays, many=True)
            if data and len(holidays) > 0:
                if len(holidays) < 4:
                    data = data.data
                else:
                    data = random.sample(data.data, k=3)

        return Response({"now": datetime.now().strftime("%d.%m.%y"), "holidays": data})
