
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
        fields = ['id', 'title_uz', 'title_en', 'content_uz', 'content_en', 'image',]


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


class abstractSerializer(serializers.ModelSerializer):

    class Meta:
        model = Abstract
        fields = ['id', 'title_uz', 'title_en', 'image', 'file']
