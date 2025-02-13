
from .models import *
from django.contrib import admin


@admin.register(Requirements)
class RequirementsAdmin(admin.ModelAdmin):
    list_display = ('title',)
    search_fields = ('title',)
    fields = ('id', 'title_uz', 'title_en', 'content_uz', 'content_en', 'sub_content_uz', 'sub_content_en',
              'image', 'order')


@admin.register(Editorial)
class EditorialAdmin(admin.ModelAdmin):
    list_display = ('title',)
    search_fields = ('title',)
    fields = ['title_uz', 'title_en', 'position_uz', 'position_en', 'degree_uz', 'degree_en', 'sphere_uz', 'sphere_en',
              'content_uz', 'content_en', 'file', 'order']


@admin.register(Archive)
class ArchiveAdmin(admin.ModelAdmin):
    list_display = ('title', 'order')
    search_fields = ('title',)
    fields = ['title_uz', 'title_en', 'year', 'image', 'file', 'order']


@admin.register(Period)
class PeriodAdmin(admin.ModelAdmin):
    list_display = ('title',)
    search_fields = ('title',)
    fields = ['title_uz', 'title_en',]


@admin.register(Books)
class BooksAdmin(admin.ModelAdmin):
    list_display = ('title', 'order')
    search_fields = ('title',)
    fields = ['title_uz', 'title_en', 'image', 'file', 'period', 'order']


@admin.register(Period_filter)
class Period_filterAdmin(admin.ModelAdmin):
    list_display = ('title',)
    search_fields = ('title',)
    fields = ['title_uz', 'title_en', ]


@admin.register(archive_documents)
class archive_documentsAdmin(admin.ModelAdmin):
    list_display = ('title',)
    search_fields = ('title',)
    fields = ['title_uz', 'title_en', 'image', 'file', 'period_filter', 'order']


@admin.register(Abstract)
class AbstractAdmin(admin.ModelAdmin):
    list_display = ('title', )
    search_fields = ('title',)
    fields = ['title_uz', 'title_en', 'image', 'file', 'order']
    # list_filter = ['category']


@admin.register(Mat_category)
class Mat_categoryAdmin(admin.ModelAdmin):
    list_display = ('title',)
    search_fields = ('title',)
    fields = ['title_uz', 'title_en',]


@admin.register(Year_filter)
class Year_filterAdmin(admin.ModelAdmin):
    list_display = ('title',)
    search_fields = ('title',)
    fields = ['title_uz', 'title_en',]


@admin.register(Region_filter)
class Region_filterAdmin(admin.ModelAdmin):
    list_display = ('title',)
    search_fields = ('title',)
    fields = ['title_uz', 'title_en']


@admin.register(the_press)
class the_pressAdmin(admin.ModelAdmin):
    list_display = ('title',)
    search_fields = ('title',)
    fields = ['title_uz', 'title_en', 'image', 'file', 'mat_cotegory', 'year_id', 'region_id', 'order']