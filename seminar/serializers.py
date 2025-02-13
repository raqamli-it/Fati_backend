from rest_framework import serializers

from .models import Seminar_turlari, Seminar


class Seminar_turlariSerializer(serializers.ModelSerializer):
    class Meta:
        model = Seminar_turlari
        fields = ('id', 'title_uz', 'title_en',)


class SeminarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Seminar
        fields = ('id', 'title_uz', 'title_en', 'content_uz', 'content_en', 'seminar_id', )

