
from rest_framework import serializers
from . models import Tahririyat, Avtoreferat, Category, Arxiv, Talablar


class TalabalarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Talablar
        fields = ('id', 'title_uz', 'title_en', 'content_uz', 'content_en', 'sub_content_uz', 'sub_content_en',
                  'image', 'status', 'order',)


class TahririyatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tahririyat
        fields = ['id', 'title_uz', 'title_en', 'position_uz', 'position_en', 'degree_uz', 'degree_en', 'sphere_uz',
                  'sphere_en', 'content_uz', 'content_en', 'file', 'status', 'order', ]


class AvtoreferatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Avtoreferat
        fields = ['id', 'title_uz', 'title_en', 'image', 'file', 'content_uz', 'content_en', 'status', 'order',
                  'category']
 

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'title_uz', 'title_en', 'status', 'order', ]


class ArxivSerializer(serializers.ModelSerializer):

    class Meta:
        model = Arxiv
        fields = ['id', 'title_uz', 'title_en', 'content_uz', 'content_en', 'image', 'status', 'order',]
