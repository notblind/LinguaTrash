import random
from datetime import datetime

from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from accounts.models import Partner
from accounts.serializers import PartnerSerializer

from .models import DayOfWeek, Holiday, Words
from .serializers import (
    FeedBackSerializer,
    HolidaySerializer,
    TranslationSerializer,
    WordSerializer,
    WordSerializerForSecondMode,
    WordSerializerForThirdMode,
)

# Create your views here.


class PartnerApi(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        method = request.data.get("method")

        if method == "get_me":
            return self.get_me(request)
        return Response({"Not allow method"})

    def get_me(self, request):
        user = request.user
        if user:
            partner = Partner.objects.get(user=user.id)
            serializer = PartnerSerializer(partner)
            return Response({"partner": serializer.data})
        return Response({"403"})


class VocabularyApi(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        method = request.data.get("method")

        if method == "get_words":
            return self.get_words(request)
        elif method == "create_word":
            return self.create_word(request)

        return Response({"Not allow method"})

    def get_words(self, request):
        idVocabulary = request.data.get("data").get("idVocabulary")

        words = Words.objects.filter(vocabulary=idVocabulary)
        serializer = WordSerializer(words, many=True)
        return Response({"words": serializer.data})

    def create_word(self, request):
        data = request.data.get("data").get("word")

        word = {"word": data["word"], "vocabulary": data["vocabulary"]}
        serializer = WordSerializer(data=word)
        if serializer.is_valid(raise_exception=True):
            res = serializer.save()
            for translate in data["translations"]:
                if translate and type(translate) == str and translate.strip() != "":
                    translate_data = {"translate": translate, "word": res.id}
                    serializer = TranslationSerializer(data=translate_data)
                    if serializer.is_valid(raise_exception=False):
                        serializer.save()
            return Response(
                {
                    "success": "Word '{}' created successfully".format(res.word),
                    "status": "success",
                }
            )


class TrainingApi(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        method = request.data.get("method")

        if method == "mode_first":
            return self.mode_first(request)
        elif method == "mode_second":
            return self.mode_second(request)
        elif method == "mode_third":
            return self.mode_third(request)

        return Response({"Not allow method"})

    def mode_first(self, request):
        idVocabulary = request.data.get("data").get("idVocabulary")
        words = sorted(
            Words.objects.filter(vocabulary=idVocabulary), key=lambda x: random.random()
        )

        serializer = WordSerializer(words, many=True)
        return Response({"training": serializer.data})

    def mode_second(self, request):
        idVocabulary = request.data.get("data").get("idVocabulary")
        words = sorted(
            Words.objects.filter(vocabulary=idVocabulary), key=lambda x: random.random()
        )

        serializer = WordSerializerForSecondMode(words, many=True)
        return Response({"training": serializer.data})

    def mode_third(self, request):
        idVocabulary = request.data.get("data").get("idVocabulary")
        words = sorted(
            Words.objects.filter(vocabulary=idVocabulary), key=lambda x: random.random()
        )
        serializer = WordSerializerForThirdMode(words, many=True)
        return Response({"training": serializer.data})


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
