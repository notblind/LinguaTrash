import random

from django.db.models import Q
from rest_framework import serializers

from vocabulary.models import Translation, Vocabulary, Word


class VocabularySerializer(serializers.ModelSerializer):
    ammount = serializers.SerializerMethodField("_ammount", read_only=True)

    class Meta:
        model = Vocabulary
        fields = ["name", "like", "partner_id", "ammount", "id", "create_time"]
        read_only_fields = ["id", "create_time"]

    def create(self, validated_data):
        return Vocabulary.objects.create(**validated_data)

    def update(self, vocabulary_id, validated_data):
        vocabulary_id.name = validated_data.get("name", vocabulary_id.name)
        vocabulary_id.like = validated_data.get("like", vocabulary_id.like)
        vocabulary_id.save()
        return vocabulary_id

    def _ammount(self, obj):
        return Word.objects.filter(vocabulary_id=obj.id).count()


class TranslationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Translation
        fields = ["id", "translate", "word_id"]
        read_only_fields = ["id"]

    def create(self, validated_data):
        return Translation.objects.create(**validated_data)


class WordSerializer(serializers.ModelSerializer):
    translations = TranslationSerializer(many=True, read_only=True)

    class Meta:
        model = Word
        fields = ["id", "word", "translations", "vocabulary_id"]
        read_only_fields = ["id"]

    def create(self, validated_data):
        return Word.objects.create(**validated_data)


class FullVocabularySerializer(serializers.ModelSerializer):
    words = WordSerializer(many=True, read_only=True)

    class Meta:
        model = Vocabulary
        fields = ["name", "like", "partner_id", "words", "id", "create_time"]
        read_only_fields = ["id", "create_time"]

    def create(self, validated_data):
        return Vocabulary.objects.create(**validated_data)

    def update(self, vocabulary_id, validated_data):
        vocabulary_id.name = validated_data.get("name", vocabulary_id.name)
        vocabulary_id.like = validated_data.get("like", vocabulary_id.like)
        vocabulary_id.save()
        return vocabulary_id


class WordSerializerForSecondMode(serializers.ModelSerializer):
    options = serializers.SerializerMethodField("_options", read_only=True)

    class Meta:
        model = Word
        fields = ["id", "word", "options", "vocabulary_id"]
        read_only_fields = ["id"]

    def _options(self, obj):
        words = sorted(
            Word.objects.filter(
                ~Q(id=obj.id) & Q(vocabulary_id=obj.vocabulary_id.id)
            ).prefetch_related("translations"),
            key=lambda x: random.random(),
        )
        options = [
            {
                "option": word.translations.all()[
                    random.randint(0, word.translations.count() - 1)
                ].translate,
                "right": False,
            }
            for word in words
        ]

        translations = obj.translations.all()
        translation = translations[random.randint(0, len(translations) - 1)]
        options.insert(
            random.randint(0, 3), {"option": translation.translate, "right": True}
        )
        return options


class WordSerializerForThirdMode(serializers.ModelSerializer):
    options = serializers.SerializerMethodField("_options", read_only=True)
    word = serializers.SerializerMethodField("_translation", read_only=True)

    class Meta:
        model = Word
        fields = ["id", "word", "options", "vocabulary_id"]
        read_only_fields = ["id"]

    def _options(self, obj):
        words = sorted(
            Word.objects.filter(
                ~Q(id=obj.id) & Q(vocabulary_id=obj.vocabulary_id.id)
            ).prefetch_related("translations"),
            key=lambda x: random.random(),
        )
        options = [{"option": word.word, "right": False} for word in words]
        options.insert(random.randint(0, 3), {"option": obj.word, "right": True})
        return options

    def _translation(self, obj):
        translations = obj.translations.all()
        translation = translations[random.randint(0, len(translations) - 1)]
        return translation.translate
