
from .models import Ilmiy_kengash_majlis, Yosh_olimlar,Azolar
from rest_framework import serializers


class Ilmiy_kengash_majlisSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ilmiy_kengash_majlis
        fields = ('id', 'title_uz', 'title_en', 'content_uz', 'content_en', 'file', 'date', 'status', 'order',)


class Yosh_olimlarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Yosh_olimlar
        fields = ('id', 'title_uz', 'title_en', 'content_uz', 'content_en', 'file', 'status', 'order',)


class AzolarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Azolar
        fields = ['id', 'name_uz', 'name_en', 'position_uz', 'position_en', 'degree_uz', 'degree_en', 'contact',
                  'email', 'status', 'order', ]