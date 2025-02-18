from django.contrib import admin
from .models import Xodimlar, Markazlar, Bolimlar, Tadqiqot, Photo, Video


@admin.register(Markazlar)
class Markazlaradmin(admin.ModelAdmin):
    list_display = ('title', 'order', 'created_at', 'updated_at')
    search_fields = ('title',)
    fields = ('title_uz', 'title_en', 'content_uz', 'content_en', 'image', 'order')


@admin.register(Bolimlar)
class Bolimlaradmin(admin.ModelAdmin):
    list_display = ('title', 'order', 'created_at', 'updated_at')
    search_fields = ('title',)
    fields = ('title_uz', 'title_en', 'content_uz', 'content_en', 'image', 'order')


@admin.register(Xodimlar)
class XodimlarAdmin(admin.ModelAdmin):
    list_display = ('ful_name', 'order', 'created_at', 'updated_at')
    search_fields = ('ful_name',)
    fields = ['ful_name_uz', 'ful_name_en', 'activity_uz', 'activity_en', 'about_uz', 'about_en', 'works_uz',
              'works_en', 'image', 'file', 'bolimlar', 'markazlar', 'order']


@admin.register(Tadqiqot)
class TadqiqotAdmin(admin.ModelAdmin):
    list_display = ('title', 'order', 'created_at', 'updated_at')
    search_fields = ('title',)
    fields = ('title_uz', 'title_en', 'content_uz', 'content_en', 'image', 'bolimlar', 'markazlar', 'order')


@admin.register(Photo)
class PhotoAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at', 'updated_at')
    search_fields = ('title',)
    fields = ('title_uz', 'title_en', 'image', 'bolimlar', 'markazlar')


@admin.register(Video)
class VideoAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at', 'updated_at')
    search_fields = ('title',)
    fields = ('title_uz', 'title_en', 'video', 'link', 'bolimlar', 'markazlar')
