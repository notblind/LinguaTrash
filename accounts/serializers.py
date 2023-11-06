from rest_framework import serializers

from .models import Partner


class PartnerSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Partner
        fields = "__all__"
