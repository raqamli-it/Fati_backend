
from .models import Ilmiy_kengash_majlis, fon_picture, Yosh_olimlar
from rest_framework import serializers
from .models import Azolar


class fon_pictureSerializer(serializers.ModelSerializer):
    class Meta:
        model = fon_picture
        fields = ('id', 'title_uz', 'title_en', 'content_uz', 'content_en', 'file', 'status', 'order', 'created_at',
                  'updated_at',)


class Ilmiy_kengash_majlisSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ilmiy_kengash_majlis
        fields = ('id', 'title_uz', 'title_en', 'content_uz', 'content_en', 'file', 'date', 'status',
                  'order', 'created_at', 'updated_at',)


class Yosh_olimlarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Yosh_olimlar
        fields = ('id', 'title_uz', 'title_en', 'content_uz', 'content_en', 'file', 'status', 'order', 'created_at',
                  'updated_at',)


class AzolarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Azolar
        fields = ['id', 'name_uz', 'name_en', 'shifr', 'ish_joy_uz', 'ish_joy_en', 'lavozim_uz', 'lavozim_en',
                  'ilmiy_darajasi_uz', 'ilmiy_darajasi_en', 'ilmiy_unvoni_uz', 'ilmiy_unvoni_en',
                  'created_at', 'updated_at', 'status', 'order', ]

#
# class DissertatsiyaIshlarSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = DissertatsiyaIshlar
#         fields = ['id', 'title_uz', 'title_en', 'file', 'content_uz', 'content_en', 'isAccepted', 'created_at',
#                   'updated_at', 'status', 'order', ]
#
