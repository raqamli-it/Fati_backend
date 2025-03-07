
from .models import Ilmiy_kengash_majlis, Yosh_olimlar, Azolar, Elonlar, Xodimlar, Kadirlar
from rest_framework import serializers


class XodimlarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Xodimlar
        fields = ('id', 'full_name_uz', 'full_name_en', 'image')
        ref_name = 'KengashlarXodimlarSerializer'


class Ilmiy_kengash_majlisSerializer(serializers.ModelSerializer):
    xodimlar = XodimlarSerializer(many=True, read_only=True)  # Remove `source='xodimlar'`

    class Meta:
        model = Ilmiy_kengash_majlis
        fields = ('id', 'title_uz', 'title_en', 'content_uz', 'content_en', 'xodimlar')


class Yosh_olimlarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Yosh_olimlar
        fields = ('id', 'title_uz', 'title_en', 'content_uz', 'content_en', 'file',)


class KadirlarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Kadirlar
        fields = ['id', 'full_name_uz', 'full_name_en', 'image', 'workplace_uz', 'workplace_en', 'position_uz',
                  'position_en', 'shifri', 'degree_uz', 'degree_en', 'academic_title_uz', 'academic_title_en',
                  'center_id']


class AzolarSerializer(serializers.ModelSerializer):
    kadirlar = KadirlarSerializer(many=True, read_only=True)

    class Meta:
        model = Azolar
        fields = ['id', 'title_uz', 'title_en', 'content_uz', 'content_en', 'kadirlar']


class ElonlarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Elonlar
        fields = ('id', 'title_uz', 'title_en', 'content_uz', 'content_en', 'image')

