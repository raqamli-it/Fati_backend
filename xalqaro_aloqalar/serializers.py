from rest_framework import serializers
from .models import Xamkor_tashkilot, Xamkor_loihalar, Xalqaro_sayohatlar
from .models import Tadqiqot


class TadqiqotSerializer(serializers.ModelSerializer):

    class Meta:
        model = Tadqiqot
        fields = ['id', 'title_uz', 'title_en', 'content_uz', 'content_en', 'img_file', 'order', ]


class Xamkor_tashkilotSerializer(serializers.ModelSerializer):
    class Meta:
        model = Xamkor_tashkilot
        fields = ('id', 'title_uz', 'title_en', 'content_uz', 'content_en', 'file',
                  'order',)


class Xamkor_loihalarSerializer(serializers.ModelSerializer):

    class Meta:
        model = Xamkor_loihalar
        fields = ('id', 'title_uz', 'title_en', 'content_uz', 'content_en',  'img_file', 'status',
                  'order',)


class Ilmiy_safarlarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Xalqaro_sayohatlar
        fields = ('id', 'title_uz', 'title_en', 'content_uz', 'content_en', 'subcontent_uz',
                  'subcontent_en', 'file', 'order', )





