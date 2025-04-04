from rest_framework import serializers
from .models import Xodimlar, Markazlar, Bolimlar, Tadqiqot, Audio, Audiolar, Rasm, Rasmlar, Video, Videolar


class XodimlarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Xodimlar
        fields = ['id', 'full_name_uz', 'full_name_en', 'surname_uz', 'surname_en', 'position_uz', 'position_en',
                  'degree_uz', 'degree_en', 'phone', 'email', 'about_uz', 'about_en', 'works_uz', 'works_en', 'image',
                  'order',]


class TadqiqotSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tadqiqot
        fields = ['id', 'title_uz', 'title_en', 'content_uz', 'content_en', 'image']


class BolimlarListSerializers(serializers.ModelSerializer):
    class Meta:
        model = Bolimlar
        fields = ['id', 'title_uz', 'title_en', 'image']


class MarkazlarListSerializers(serializers.ModelSerializer):
    class Meta:
        model = Markazlar
        fields = ['id', 'title_uz', 'title_en', 'image']


class MarkazlarSerializer(serializers.ModelSerializer):
    xodim = XodimlarSerializer(many=True, read_only=True)
    tadqiqotlar = TadqiqotSerializer(many=True, read_only=True)
    # photos = PhotoSerializer(many=True, read_only=True)
    # videos = VideoSerializer(many=True, read_only=True)

    class Meta:
        model = Markazlar
        fields = ['id', 'title_uz', 'title_en', 'content_uz', 'content_en', 'content_two_uz', 'content_two_en', 'image', 'file', 'order',
                  'xodim', 'tadqiqotlar',]


class BolimlarSerializer(serializers.ModelSerializer):
    xodimlar = XodimlarSerializer(many=True, read_only=True)
    tadqiqot = TadqiqotSerializer(many=True, read_only=True)
    # photo = PhotoSerializer(many=True, read_only=True)
    # video = VideoSerializer(many=True, read_only=True)

    class Meta:
        model = Bolimlar
        fields = ['id', 'title_uz', 'title_en', 'content_uz', 'content_en', 'content_two_uz', 'content_two_en', 'image', 'file', 'order',
                  'xodimlar', 'tadqiqot',]


class AudiolarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Audiolar
        fields = ['id', 'audio']


class AudioSerializer(serializers.ModelSerializer):
    # audiolar = AudiolarSerializer(many=True, read_only=True, source='Audiolar')

    class Meta:
        model = Audio
        fields = ['id', 'title_uz', 'title_en', 'audio', 'image', 'order']


class RasmlarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rasmlar
        fields = ['id', 'image']


class RasmSerializer(serializers.ModelSerializer):
    rasmlar = RasmlarSerializer(many=True, read_only=True, source='Rasmlar')

    class Meta:
        model = Rasm
        fields = ['id', 'title_uz', 'title_en', 'image', 'rasmlar']


class VideolarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Videolar
        fields = ['id', 'video']


class VideoSerializer(serializers.ModelSerializer):
    # videolar = VideolarSerializer(many=True, read_only=True, source='Videolar')

    class Meta:
        model = Video
        fields = ['id', 'title_uz', 'title_en', 'video', 'image', 'link', 'order']



