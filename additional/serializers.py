from rest_framework import serializers

from additional.models import FeedBack, Holiday


class FeedBackSerializer(serializers.ModelSerializer):
    class Meta:
        model = FeedBack
        fields = ["text"]

    def create(self, validated_data):
        return FeedBack.objects.create(**validated_data)


class HolidaySerializer(serializers.ModelSerializer):
    class Meta:
        model = Holiday
        fields = ["description"]
