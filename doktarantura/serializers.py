from .models import Qabul_tartibi, Malakaviy_imtihon, Doktarantura
from rest_framework import serializers


class Qabul_tartibiSerializer(serializers.ModelSerializer):
    class Meta:
        model = Qabul_tartibi
        fields = ('id', 'title_uz', 'title_en', 'content_uz', 'content_en', 'file', 'status', 'order', 'created_at',
                  'updated_at',)


class Malakaviy_imtihonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Malakaviy_imtihon
        fields = ('id', 'title_uz', 'title_en', 'content_uz', 'content_en', 'file', 'status', 'order', 'created_at',
                  'updated_at',)


class DoktaranturaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Doktarantura
        fields = ('id', 'title_uz', 'title_en', 'labor_activity_uz', 'labor_activity_en', 'scientific_activity_uz',
                  'scientific_activity_en', 'works_uz', 'works_en', 'file', 'type', 'status', 'order')



