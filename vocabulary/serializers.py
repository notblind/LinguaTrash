from rest_framework import serializers

from accounts.models import Partner
from .models import Vocabulary, Words, Translation

import logging

class VocabularySerializer(serializers.Serializer):
	id = serializers.IntegerField(label='ID', read_only=True)
	name = serializers.CharField(max_length=2048)
	create_time = serializers.DateField(required=False)
	like = serializers.BooleanField(required=False)
	ammount = serializers.SerializerMethodField('_ammount', read_only=True)
	partner = serializers.PrimaryKeyRelatedField(queryset=Partner.objects.all())

	def create(self, validated_data):
		return Vocabulary.objects.create(**validated_data)

	def update(self, vocabulary, validated_data):
		vocabulary.name = validated_data.get('name', vocabulary.name)
		vocabulary.like = validated_data.get('like', vocabulary.like)
		vocabulary.save()
		return vocabulary

	def _ammount(self, obj):
		words = Words.objects.filter(vocabulary=obj.id)
		return len(words)

class WordSerializer(serializers.Serializer):
	id = serializers.IntegerField(label='ID', read_only=True)
	word = serializers.CharField(max_length=2048)
	translations = serializers.SerializerMethodField('get_translations', read_only=True)
	vocabulary = serializers.PrimaryKeyRelatedField(queryset=Vocabulary.objects.all())

	def create(self, validated_data):
		return Words.objects.create(**validated_data)

	def get_translations(self, obj):
		translations = Translation.objects.filter(word=obj.id)

		serializer = TranslationSerializer(translations, many=True)

		logging.error(serializer)
		return serializer.data

class TranslationSerializer(serializers.Serializer):
	id = serializers.IntegerField(label='ID', read_only=True)
	translate = serializers.CharField(max_length=2048)
	word = serializers.PrimaryKeyRelatedField(queryset=Words.objects.all())

	def create(self, validated_data):
		return Translation.objects.create(**validated_data)
		