
from .models import Ilmiy_kengash_majlis, Yosh_olimlar, Azolar, Elonlar
from rest_framework import serializers


class Ilmiy_kengash_majlisSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ilmiy_kengash_majlis
        fields = ('id', 'title_uz', 'title_en', 'content_uz', 'content_en',)


class Yosh_olimlarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Yosh_olimlar
        fields = ('id', 'title_uz', 'title_en', 'content_uz', 'content_en', 'file',)


class AzolarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Azolar
        fields = ['id', 'title_uz', 'title_en', 'content_uz', 'content_en',]


class ElonlarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Elonlar
        fields = ('id', 'title_uz', 'title_en', 'content_uz', 'content_en', 'image')

