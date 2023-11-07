import logging
import random

from django.db.models import Q
from rest_framework import serializers

from accounts.models import Partner

from .models import FeedBack, Holiday, Translation, Vocabulary, Words


class VocabularySerializer(serializers.ModelSerializer):
    ammount = serializers.SerializerMethodField("_ammount", read_only=True)

    class Meta:
        model = Vocabulary
        fields = ["name", "like", "partner", "ammount", "id", "create_time"]
        read_only_fields = ["id", "create_time"]

    def create(self, validated_data):
        return Vocabulary.objects.create(**validated_data)

    def update(self, vocabulary, validated_data):
        vocabulary.name = validated_data.get("name", vocabulary.name)
        vocabulary.like = validated_data.get("like", vocabulary.like)
        vocabulary.save()
        return vocabulary

    def _ammount(self, obj):
        words = Words.objects.filter(vocabulary=obj.id)
        return len(words)


class FullVocabularySerializer(serializers.ModelSerializer):
    ammount = serializers.SerializerMethodField("_ammount", read_only=True)
    words = serializers.SerializerMethodField("get_words", read_only=True)

    class Meta:
        model = Vocabulary
        fields = ["name", "like", "partner", "ammount", "words", "id", "create_time"]
        read_only_fields = ["id", "create_time"]

    def create(self, validated_data):
        return Vocabulary.objects.create(**validated_data)

    def get_words(self, obj):
        words = Words.objects.filter(vocabulary=obj.id)
        serializer = WordSerializer(words, many=True)
        return serializer.data

    def update(self, vocabulary, validated_data):
        vocabulary.name = validated_data.get("name", vocabulary.name)
        vocabulary.like = validated_data.get("like", vocabulary.like)
        vocabulary.save()
        return vocabulary

    def _ammount(self, obj):
        words = Words.objects.filter(vocabulary=obj.id)
        return len(words)


class TranslationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Translation
        fields = ["id", "translate", "word"]
        read_only_fields = ["id"]

    def create(self, validated_data):
        return Translation.objects.create(**validated_data)


class WordSerializer(serializers.ModelSerializer):
    translations = TranslationSerializer(many=True, read_only=True)

    class Meta:
        model = Words
        fields = ["id", "word", "translations", "vocabulary"]
        read_only_fields = ["id"]

    def create(self, validated_data):
        return Words.objects.create(**validated_data)


class WordSerializerForSecondMode(serializers.ModelSerializer):
    options = serializers.SerializerMethodField("_options", read_only=True)

    class Meta:
        model = Words
        fields = ["id", "word", "options", "vocabulary"]
        read_only_fields = ["id"]

    def _options(self, obj):
        words = sorted(
            Words.objects.filter(~Q(id=obj.id) & Q(vocabulary=obj.vocabulary.id)),
            key=lambda x: random.random(),
        )
        index = 3
        options = []
        if len(words) < 3:
            index = len(words)

        for i in range(0, index):
            word = words[i]

            translations = Translation.objects.filter(word=word.id)
            translation = translations[random.randint(0, len(translations) - 1)]
            options.append({"option": translation.translate, "right": False})

        translations = Translation.objects.filter(word=obj.id)
        translation = translations[random.randint(0, len(translations) - 1)]
        options.insert(
            random.randint(0, index), {"option": translation.translate, "right": True}
        )
        return options


class WordSerializerForThirdMode(serializers.ModelSerializer):
    options = serializers.SerializerMethodField("_options", read_only=True)
    word = serializers.SerializerMethodField("_translation", read_only=True)

    class Meta:
        model = Words
        fields = ["id", "word", "options", "vocabulary"]
        read_only_fields = ["id"]

    def _options(self, obj):
        words = sorted(
            Words.objects.filter(~Q(id=obj.id) & Q(vocabulary=obj.vocabulary.id)),
            key=lambda x: random.random(),
        )
        index = 3
        options = []
        if len(words) < 3:
            index = len(words)

        for i in range(0, index):
            options.append({"option": words[i].word, "right": False})
        options.insert(random.randint(0, index), {"option": obj.word, "right": True})
        return options

    def _translation(self, obj):
        translations = Translation.objects.filter(word=obj.id)
        translation = translations[random.randint(0, len(translations) - 1)]
        return translation.translate


class FeedBackSerializer(serializers.ModelSerializer):
    class Meta:
        model = FeedBack
        fields = ["text", "partner", "create_time"]
        read_only_fields = ["create_time"]

    def create(self, validated_data):
        return FeedBack.objects.create(**validated_data)


class HolidaySerializer(serializers.ModelSerializer):
    class Meta:
        model = Holiday
        fields = ["description"]
