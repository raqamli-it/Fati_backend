
from .models import Talablar
from .models import Arxiv
from rest_framework import serializers
from . models import Tahrirchi, Avtoreferat, Manba, ElektronKitob


class TalabalarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Talablar
        fields = ('id', 'title_uz', 'title_en', 'content_uz', 'content_en', 'img_url',
                  'status', 'order', 'created_at', 'Updated_at')


class TahrirchiSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tahrirchi
        fields = ['id', 'title_uz', 'title_en', 'ish_joyi', 'lavozimi', 'status', 'order', 'created_at', 'Updated_at',]



class AvtoreferatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Avtoreferat
        fields = ['title_uz', 'title_en', 'cover_img', 'file', 'status', 'order', 'created_at', 'Updated_at']


class ElektronKitobSerializer(serializers.ModelSerializer):
    class Meta:
        model = ElektronKitob
        fields = ['title_uz', 'title_en', 'cover_img', 'file', 'status', 'order', 'created_at', 'Updated_at']


class ManbaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Manba
        fields = ['title_uz', 'title_en', 'cover_img', 'file', 'status', 'order', 'created_at', 'Updated_at']


class ArxivSerializer(serializers.ModelSerializer):

    class Meta:
        model = Arxiv
        fields = ['id', 'title_uz', 'title_en', 'yil', 'nashr_raqami', 'content_uz', 'content_en', 'image', 'status',
                  'order', 'created_at', 'Updated_at',]



