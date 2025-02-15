
from rest_framework import serializers
from . models import *


class RequirementsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Requirements
        fields = ('id', 'title_uz', 'title_en', 'content_uz', 'content_en', 'sub_content_uz', 'sub_content_en',
                  'image',)


class EditorialSerializer(serializers.ModelSerializer):
    class Meta:
        model = Editorial
        fields = ['id', 'title_uz', 'title_en', 'position_uz', 'position_en', 'degree_uz', 'degree_en', 'sphere_uz',
                  'sphere_en', 'content_uz', 'content_en', 'file',]


class ArchiveSerializer(serializers.ModelSerializer):

    class Meta:
        model = Archive
        fields = ['id', 'title_uz', 'title_en', 'year', 'image', 'file']


class SourcesSerializer(serializers.ModelSerializer):

    class Meta:
        model = Sources
        fields = ['id', 'title_uz', 'title_en', 'image', 'file',]


class LiteratureSerializer(serializers.ModelSerializer):

    class Meta:
        model = Literature
        fields = ['id', 'title_uz', 'title_en', 'image', 'file',]


class Archive_documentsSerializer(serializers.ModelSerializer):
    image = serializers.SerializerMethodField()
    file = serializers.SerializerMethodField()

    class Meta:
        model = Archive_documents
        fields = ['id', 'title_uz', 'title_en', 'image', 'file']

    def get_image(self, obj):
        request = self.context.get('request')
        if obj.image:
            return request.build_absolute_uri(obj.image.url) if request else obj.image.url
        return None

    def get_file(self, obj):
        request = self.context.get('request')
        if obj.file:
            return request.build_absolute_uri(obj.file.url) if request else obj.file.url
        return None


class abstractSerializer(serializers.ModelSerializer):

    class Meta:
        model = Abstract
        fields = ['id', 'title_uz', 'title_en', 'image', 'file']


#
#
# class CommentSerializer(serializers.ModelSerializer):
#
#     class Meta:
#         model = Comment
#         fields = ['id', 'title', 'text', 'file']