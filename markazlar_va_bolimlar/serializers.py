from rest_framework import serializers
from .models import Xodimlar, Markazlar, Bolimlar, Tadqiqot, Photo, Video


class XodimlarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Xodimlar
        fields = ['id', 'ful_name_uz', 'ful_name_en', 'activity_uz', 'activity_en',
                  'about_uz', 'about_en', 'works_uz', 'works_en', 'image', 'order',]


class TadqiqotSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tadqiqot
        fields = ['id', 'title_uz', 'title_en', 'content_uz', 'content_en', 'image']


class PhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Photo
        fields = ['id', 'title_uz', 'title_en', 'image']


class VideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Video
        fields = ['id', 'title_uz', 'title_en', 'video', 'link']


# List
class BolimlarListSerializers(serializers.ModelSerializer):
    class Meta:
        model = Bolimlar
        fields = ['id', 'title_uz', 'title_en', ]


class MarkazlarListSerializers(serializers.ModelSerializer):
    class Meta:
        model = Markazlar
        fields = ['id', 'title_uz', 'title_en', ]


# detail
class MarkazlarSerializer(serializers.ModelSerializer):
    xodim = XodimlarSerializer(many=True, read_only=True)
    tadqiqotlar = TadqiqotSerializer(many=True, read_only=True)
    photos = PhotoSerializer(many=True, read_only=True)
    videos = VideoSerializer(many=True, read_only=True)

    class Meta:
        model = Markazlar
        fields = ['id', 'title_uz', 'title_en', 'content_uz', 'content_en', 'image', 'order',
                  'xodim', 'tadqiqotlar', 'photos', 'videos']


class BolimlarSerializer(serializers.ModelSerializer):
    xodimlar = XodimlarSerializer(many=True, read_only=True)
    tadqiqot = TadqiqotSerializer(many=True, read_only=True)
    photo = PhotoSerializer(many=True, read_only=True)
    video = VideoSerializer(many=True, read_only=True)

    class Meta:
        model = Bolimlar
        fields = ['id', 'title_uz', 'title_en', 'content_uz', 'content_en', 'image', 'order',
                  'xodimlar', 'tadqiqot', 'photo', 'video']
