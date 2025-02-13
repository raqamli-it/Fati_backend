from django.contrib import admin

from .models import Seminar_turlari, Seminar


@admin.register(Seminar_turlari)
class Seminar_turlariAdmin(admin.ModelAdmin):
    list_display = ('title',)
    search_fields = ('title',)
    fields = ['title_uz', 'title_en',]


@admin.register(Seminar)
class SeminarAdmin(admin.ModelAdmin):
    list_display = ('title',)
    search_fields = ('title',)
    fields = ['title_uz', 'title_en', 'content_uz', 'content_en', 'seminar_id',]

