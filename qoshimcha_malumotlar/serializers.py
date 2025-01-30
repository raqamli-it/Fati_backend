
from rest_framework import serializers

from qoshimcha_malumotlar.models import Institut_tarixi, Aloqa, Karusel, Rahbariyat, Tashkiliy_tuzulma, Yangiliklar, \
     Havolalar, Direktorlar


class DirektorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Direktorlar
        fields = ('id', 'title_uz', 'title_en', 'image', 'about', )


class Institut_tarixiSerializer(serializers.ModelSerializer):
    Direktor = DirektorSerializer(many=True, read_only=True)

    class Meta:
        model = Institut_tarixi
        fields = ('id', 'title_uz', 'title_en', 'content_uz', 'content_en', 'image', 'status', 'order', 'Direktor')


class AloqaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Aloqa
        fields = ('id', 'faks', 'email', 'phone', 'adress', 'lat', 'long', 'youtube', 'telegram', 'instagram',
                  'facebook', 'status', 'order',)


class KaruselSerializer(serializers.ModelSerializer):
    class Meta:
        model = Karusel
        fields = ('id',  'file', 'link',)


class RahbariyatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rahbariyat
        fields = ('id', 'title_uz', 'title_en', 'position', 'degree', 'contact', 'days', 'image', 'status', 'order',)


class Tashkiliy_tuzulmaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tashkiliy_tuzulma
        fields = ('id', 'title_uz', 'title_en', 'content_uz', 'content_en', 'file', 'status', 'order', )


class YangiliklarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Yangiliklar
        fields = ('id', 'title_uz', 'title_en', 'content_uz', 'content_en', 'image', 'status', 'order',)


class HavolalarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Havolalar
        fields = ('id', 'title_uz', 'title_en', 'file', 'link', 'status', 'order',)


