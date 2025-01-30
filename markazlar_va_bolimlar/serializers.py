
from rest_framework import serializers
from .models import Xodimlar, Markazlar_Bolimlar, Tadqiqot, Photo, Video


class MarkazlarBolimlarSerializer(serializers.ModelSerializer):

    class Meta:
        model = Markazlar_Bolimlar
        fields = ['id', 'title_uz', 'title_en', 'content_uz', 'content_en', 'image', 'status', 'order']


class Markazlar_BolimlarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Markazlar_Bolimlar
        fields = ['id', 'title_uz', 'title_en',]


class XodimlarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Xodimlar
        fields = ['id', 'title_uz', 'title_en', 'sphere_uz', 'sphere_en',
                  'position_uz', 'position_en', 'academic_degree_uz', 'academic_degree_en',
                  'email', 'image', 'about_uz', 'about_en', 'works_uz', 'works_en',
                  'status', 'order', 'center_id']


class Tadqiqot_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Tadqiqot
        fields = ['id', 'title_uz', 'title_en', 'content_uz', 'content_en', 'image', 'center_id']


class PhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Photo
        fields = ['id', 'title_uz', 'title_en', 'image', 'center_id']


class VideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Video
        fields = ['id', 'title_uz', 'title_en', 'video', 'link', 'center_id']