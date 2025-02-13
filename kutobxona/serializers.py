
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


class BooksSerializer(serializers.ModelSerializer):

    class Meta:
        model = Books
        fields = ['id', 'title_uz', 'title_en', 'image', 'file',]


class PeriodListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Period
        fields = ['id', 'title_uz', 'title_en',]


class PeriodDetailSerializer(serializers.ModelSerializer):
    books = BooksSerializer(many=True, read_only=True)

    class Meta:
        model = Period
        fields = ['id', 'title_uz', 'title_en', 'books']


class Period_filterSerializer(serializers.ModelSerializer):

    class Meta:
        model = Period_filter
        fields = ['id', 'title_uz', 'title_en',]


class archive_documentsSerializer(serializers.ModelSerializer):

    class Meta:
        model = archive_documents
        fields = ['id', 'title_uz', 'title_en', 'image', 'file']


class abstractSerializer(serializers.ModelSerializer):

    class Meta:
        model = Abstract
        fields = ['id', 'title_uz', 'title_en', 'image', 'file']


class Mat_categorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Mat_category
        fields = ['id', 'title_uz', 'title_en',]


class Year_filterSerializer(serializers.ModelSerializer):

    class Meta:
        model = Year_filter
        fields = ['id', 'title_uz', 'title_en',]


class Region_filterSerializer(serializers.ModelSerializer):

    class Meta:
        model = Region_filter
        fields = ['id', 'title_uz', 'title_en',]


class the_pressSerializer(serializers.ModelSerializer):
    mat_category = Mat_categorySerializer(read_only=True)
    year_filter = Year_filterSerializer(read_only=True)
    region_filter = Region_filterSerializer(read_only=True)

    class Meta:
        model = the_press
        fields = ['id', 'title_uz', 'title_en', 'image', 'file', 'mat_category', 'year_filter', 'region_filter']


class CommentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Comment
        fields = ['id', 'title', 'text', 'file']