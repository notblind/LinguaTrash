from rest_framework import serializers
from django.db.models import Q

from accounts.models import Partner
from .models import Vocabulary, Words, Translation

import logging
import random

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
		return serializer.data

class TranslationSerializer(serializers.Serializer):
	id = serializers.IntegerField(label='ID', read_only=True)
	translate = serializers.CharField(max_length=2048)
	word = serializers.PrimaryKeyRelatedField(queryset=Words.objects.all())

	def create(self, validated_data):
		return Translation.objects.create(**validated_data)

class WordSerializerForSecondMode(serializers.Serializer):
	id = serializers.IntegerField(label='ID', read_only=True)
	word = serializers.CharField(max_length=2048)
	options = serializers.SerializerMethodField('_options', read_only=True)
	vocabulary = serializers.PrimaryKeyRelatedField(queryset=Vocabulary.objects.all())

	def _options(self, obj):
		words = sorted(Words.objects.filter(~Q(id=obj.id) & Q(vocabulary=obj.vocabulary.id)), key=lambda x: random.random())
		index = 3
		options = []
		if len(words) < 3:
			index = len(words)

		for i in range(0, index):
			word = words[i]

			translations = Translation.objects.filter(word=word.id)
			translation = translations[random.randint(0, len(translations)-1)]
			options.append({'option': translation.translate, 'right': False})

		translations = Translation.objects.filter(word=obj.id)
		translation = translations[random.randint(0, len(translations)-1)]
		options.insert(random.randint(0, index), {'option': translation.translate, 'right': True})
		return options

class WordSerializerForThirdMode(serializers.Serializer):
	id = serializers.IntegerField(label='ID', read_only=True)
	options = serializers.SerializerMethodField('_options', read_only=True)
	vocabulary = serializers.PrimaryKeyRelatedField(queryset=Vocabulary.objects.all())
	word = serializers.SerializerMethodField('_translation', read_only=True)

	def _options(self, obj):
		words = sorted(Words.objects.filter(~Q(id=obj.id) & Q(vocabulary=obj.vocabulary.id)), key=lambda x: random.random())
		index = 3
		options = []
		if len(words) < 3:
			index = len(words)

		for i in range(0, index):
			options.append({'option': words[i].word, 'right': False})
		options.insert(random.randint(0, index), {'option': obj.word, 'right': True})
		return options

	def _translation(self, obj):
		translations = Translation.objects.filter(word=obj.id)
		translation = translations[random.randint(0, len(translations)-1)]
		return translation.translate