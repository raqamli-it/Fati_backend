
from django.contrib import admin
from .models import Xodimlar, Markazlar_Bolimlar, Tadqiqot, Photo, Video


@admin.register(Markazlar_Bolimlar)
class Markazlar_Bolimlar(admin.ModelAdmin):
    list_display = ('title', 'status', 'order', 'created_at', 'updated_at',)
    search_fields = ('title',)
    fields = ('title_uz', 'title_en', 'content_uz', 'content_en', 'image', 'status', 'order',)


@admin.register(Xodimlar)
class XodimlarAdmin(admin.ModelAdmin):
    list_display = ('title', 'status', 'order', 'created_at', 'updated_at')
    search_fields = ('title',)
    fields = ['title_uz', 'title_en', 'birth', 'sphere_uz', 'sphere_en',
              'position_uz', 'position_en', 'academic_degree_uz', 'academic_degree_en',
              'email', 'image', 'about_uz', 'about_en', 'works_uz', 'works_en',
              'batafsil', 'status', 'order', 'center_id']


@admin.register(Tadqiqot)
class TadqiqotAdmin(admin.ModelAdmin):
    list_display = ('title', 'status', 'order', 'created_at', 'updated_at')
    search_fields = ('title',)
    fields = ('title_uz', 'title_en', 'content_uz', 'content_en', 'image', 'status', 'order', 'center_id', )


@admin.register(Photo)
class PhotoAdmin(admin.ModelAdmin):
    list_display = ('title', 'image', 'status', 'order', 'created_at', 'updated_at')
    search_fields = ('title',)
    fields = ('title_uz', 'title_en', 'image', 'status', 'order', 'center_id',)


@admin.register(Video)
class VideoAdmin(admin.ModelAdmin):
    list_display = ('title', 'status', 'order', 'created_at', 'updated_at')
    search_fields = ('title',)
    fields = ('title_uz', 'title_en', 'video', 'link', 'status', 'order', 'center_id',)