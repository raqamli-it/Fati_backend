
from rest_framework import serializers
from .models import Xodimlar, MarkazlarBolimlar, Rasmlar


class XodimlarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Xodimlar
        fields = ('id', 'name_uz', 'name_en', 'lavozim_uz', 'lavozim_en', 'ilmiy_daraja_uz', 'ilmiy_daraja_en',
                  'markazlar_bolimlar', 'status', 'order', 'created_at', 'updated_at')


class RasmlarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rasmlar
        fields = ('id', 'fotogalereya', 'silder')


class MarkazlarBolimlarSerializer(serializers.ModelSerializer):
    rasmlar = RasmlarSerializer(many=True, read_only=True)
    xodimlar = XodimlarSerializer(many=True)

    class Meta:
        model = MarkazlarBolimlar
        fields = ('id', 'title_uz', 'title_en', 'tarix_uz', 'tarix_en', 'rasmlar', 'xodimlar', 'status',
                  'order', 'created_at', 'updated_at')


