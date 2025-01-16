
from .models import Talablar
from .models import Tahrirchi, Avtoreferat, Manba, ElektronKitob
from django.contrib import admin
from .models import Arxiv


@admin.register(Talablar)
class RequirementsAdmin(admin.ModelAdmin):
    list_display = ('title', 'status', 'created_at', 'Updated_at', 'order',)
    search_fields = ('title',)
    fields = ('title_uz', 'title_en', 'content_uz', 'content_en',
              'img_url', 'status', 'order',)


@admin.register(Tahrirchi)
class TahrirchiAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at', 'Updated_at', 'order',)
    search_fields = ('title',)
    fields = ['title_uz', 'title_en', 'ish_joyi', 'lavozimi', 'status', 'order',]


@admin.register(Avtoreferat)
class AvtoreferatAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at', 'Updated_at', 'order',)
    search_fields = ('title',)
    fields = ['title_uz', 'title_en', 'cover_img', 'file', 'status', 'order',]


@admin.register(ElektronKitob)
class ElektronKitobAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at', 'Updated_at', 'order',)
    search_fields = ('title',)
    fields = ['title_uz', 'title_en', 'cover_img', 'file', 'status', 'order',]


@admin.register(Manba)
class ManbalarAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at', 'Updated_at', 'order',)
    search_fields = ('title',)
    fields = ['title_uz', 'title_en', 'cover_img', 'file', 'status', 'order',]


@admin.register(Arxiv)
class ArxivAdmin(admin.ModelAdmin):
    list_display = ('title', 'yil', 'nashr_raqami', 'status', 'order', 'created_at', 'Updated_at')
    fields = ['title_uz', 'title_en', 'yil', 'nashr_raqami', 'content_uz', 'content_en', 'image', 'status', 'order',]
