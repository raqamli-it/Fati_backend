from django.contrib import admin
from .models import Xamkor_tashkilot, Xamkor_loihalar, Xalqaro_sayohatlar
from .models import Tadqiqot


@admin.register(Xamkor_tashkilot)
class Xamkor_tashkilotAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at', 'updated_at', 'order',)
    search_fields = ('title',)
    fields = ['title_uz', 'title_en', 'content_uz', 'content_en', 'file', 'order',]



@admin.register(Xamkor_loihalar)
class Xamkor_loihalarAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at', 'updated_at', 'order',)
    search_fields = ('title',)
    fields = ['title_uz', 'title_en', 'content_uz', 'content_en', 'img_file', 'order',]


@admin.register(Xalqaro_sayohatlar)
class Xalqaro_sayohatlarAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at', 'updated_at', 'order',)
    search_fields = ('title',)
    fields = ['title_uz', 'title_en', 'content_uz', 'content_en', 'subcontent_uz', 'subcontent_en', 'file', 'order',]


@admin.register(Tadqiqot)
class TadqiqotAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at', 'updated_at', 'order',)
    search_fields = ('title',)
    fields = ['title_uz', 'title_en', 'content_uz', 'content_en', 'img_file', 'order', ]