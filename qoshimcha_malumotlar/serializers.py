
from rest_framework import serializers

from .models import Institut_tarixi, Aloqa, Karusel, Rahbariyat, Tashkiliy_tuzulma, Yangiliklar, \
     Havolalar, Direktorlar, Xabarlar


class DirektorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Direktorlar
        fields = ('id', 'title_uz', 'title_en', 'image', 'about', )


class Institut_tarixiSerializer(serializers.ModelSerializer):
    direktorlar = DirektorSerializer(many=True, read_only=True, source='Direktorlar')

    class Meta:
        model = Institut_tarixi
        fields = ('id', 'title_uz', 'title_en', 'content_uz', 'content_en', 'image', 'order', 'direktorlar')


class AloqaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Aloqa
        fields = ('id', 'phone', 'email', 'adress', 'lat', 'long', 'youtube', 'telegram', 'instagram',
                  'facebook',)


class XabarlarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Xabarlar
        fields = ['id', 'name', 'phone', 'content']


class KaruselSerializer(serializers.ModelSerializer):
    class Meta:
        model = Karusel
        fields = ('id',  'file', 'link',)


class RahbariyatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rahbariyat
        fields = ('id', 'title_uz', 'title_en', 'position', 'degree', 'contact', 'days', 'image', 'order',)


class Tashkiliy_tuzulmaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tashkiliy_tuzulma
        fields = ('id', 'title_uz', 'title_en', 'content_uz', 'content_en', 'file', 'order', )


class YangiliklarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Yangiliklar
        fields = ('id', 'title_uz', 'title_en', 'content_uz', 'content_en', 'image', 'order', 'created_at', 'updated_at')


class HavolalarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Havolalar
        fields = ('id', 'title_uz', 'title_en', 'file', 'link', 'order',)
