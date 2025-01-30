from rest_framework import serializers
from xalqaro_aloqalar.models import Xamkor_tashkilot, Xamkor_loihalar, Xalqaro_sayohatlar
from xalqaro_aloqalar.models import Tadqiqot


class TadqiqotSerializer(serializers.ModelSerializer):

    class Meta:
        model = Tadqiqot
        fields = ['id', 'title_uz', 'title_en', 'content_uz', 'content_en', 'img_file', 'status', 'order', ]


class Xamkor_tashkilotSerializer(serializers.ModelSerializer):
    class Meta:
        model = Xamkor_tashkilot
        fields = ('id', 'title_uz', 'title_en', 'content_uz', 'content_en', 'file',
                  'status', 'order', 'created_at', 'updated_at',)


class Xamkor_loihalarSerializer(serializers.ModelSerializer):
    # xamkor_loiha = xamkor_loyihalar_dataSerializer()

    class Meta:
        model = Xamkor_loihalar
        fields = ('id', 'title_uz', 'title_en', 'content_uz', 'content_en',  'img_file',
                  'status', 'order', 'created_at', 'updated_at')


class Xamkor_loihalarGroupedSerializer(serializers.Serializer):
    published = serializers.SerializerMethodField()
    unpublished = serializers.SerializerMethodField()

    def get_published(self, obj):
        published_projects = obj.filter(status='published')
        return Xamkor_loihalarSerializer(published_projects, many=True).data

    def get_unpublished(self, obj):
        unpublished_projects = obj.filter(status='not_published')
        return Xamkor_loihalarSerializer(unpublished_projects, many=True).data


class Xalqaro_sayohatlarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Xalqaro_sayohatlar
        fields = ('id', 'title_uz', 'title_en', 'content_uz', 'content_en', 'subcontent_uz',
                  'subcontent_en', 'file', 'status', 'order', 'created_at', 'updated_at',)





