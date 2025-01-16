
from rest_framework import serializers

from qoshimcha_malumotlar.models import Institut_tarixi, Aloqa, Karusel, Rahbariyat, Tashkiliy_tuzulma, Yangiliklar, \
     Havolalar, picture, Kengash_rasm


class pictureSerializer(serializers.ModelSerializer):
    class Meta:
        model = picture
        fields = ('id', 'news', 'about_institute')


class Kengash_rasmSerializer(serializers.ModelSerializer):
    class Meta:
        model = Kengash_rasm
        fields = ('id', 'title_uz', 'title_en', 'picture', 'content_uz', 'content_en',)


class Institut_tarixiSerializer(serializers.ModelSerializer):
    class Meta:
        model = Institut_tarixi
        fields = ('id', 'title_uz', 'title_en', 'content_uz', 'content_en', 'subcontent_uz', 'subcontent_en', 'file',
                  'base_file', 'status', 'order', 'created_at', 'updated_at',)


class AloqaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Aloqa
        fields = ('id', 'faks', 'email', 'phone', 'adress', 'lat', 'long', 'youtube', 'telegram', 'instagram',
                  'facebook', 'status', 'order', 'created_at', 'updated_at',)


class KaruselSerializer(serializers.ModelSerializer):
    class Meta:
        model = Karusel
        fields = ('id',  'file', 'link',)


class RahbariyatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rahbariyat
        fields = ('id', 'title_uz', 'title_en', 'position', 'degree', 'contact', 'days', 'image', 'status', 'order',
                  'created_at', 'updated_at',)


class Tashkiliy_tuzulmaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tashkiliy_tuzulma
        fields = ('id', 'title_uz', 'title_en', 'content_uz', 'content_en', 'file', 'status', 'order', 'created_at',
                  'updated_at',)


class YangiliklarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Yangiliklar
        fields = ('id', 'title_uz', 'title_en', 'content_uz', 'content_en', 'subcontent_uz', 'subcontent_en', 'file',
                  'status', 'order', 'created_at', 'updated_at',)


class HavolalarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Havolalar
        fields = ('id', 'title_uz', 'title_en', 'file', 'link', 'status', 'order', 'created_at', 'updated_at',)


