
from .models import *
from django.contrib import admin


@admin.register(Requirements)
class RequirementsAdmin(admin.ModelAdmin):
    list_display = ('title', 'order')
    search_fields = ('title',)
    fields = ('title_uz', 'title_en', 'content_uz', 'content_en', 'sub_content_uz', 'sub_content_en',
              'image', 'order')


@admin.register(Editorial)
class EditorialAdmin(admin.ModelAdmin):
    list_display = ('title', 'order')
    search_fields = ('title',)
    fields = ['title_uz', 'title_en', 'content_uz', 'content_en', 'image', 'order']


@admin.register(Archive)
class ArchiveAdmin(admin.ModelAdmin):
    list_display = ('title', 'order')
    search_fields = ('title',)
    fields = ['title_uz', 'title_en', 'year', 'image', 'file', 'order']


@admin.register(Sources)
class SourcesAdmin(admin.ModelAdmin):
    list_display = ('title', 'order')
    search_fields = ('title',)
    fields = ['title_uz', 'title_en', 'title_two_uz', 'title_two_en', 'image', 'file', 'order']


@admin.register(Literature)
class LiteratureAdmin(admin.ModelAdmin):
    list_display = ('title', 'order')
    search_fields = ('title',)
    fields = ['title_uz', 'title_en', 'title_two_uz', 'title_two_en', 'image', 'file', 'order']


@admin.register(Abstract)
class AbstractAdmin(admin.ModelAdmin):
    list_display = ('title', 'order')
    search_fields = ('title',)
    fields = ['title_uz', 'title_en', 'title_two_uz', 'title_two_en', 'image', 'file', 'order']