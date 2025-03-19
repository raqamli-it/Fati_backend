from django.contrib import admin
from .models import Qabul_tartibi, Malakaviy_imtihon, Doktarantura


@admin.register(Qabul_tartibi)
class Qabul_tartibiAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at', 'updated_at', 'order',)
    search_fields = ('title',)
    fields = ('title_uz', 'title_en', 'content_uz', 'content_en', 'file', 'order',)


@admin.register(Malakaviy_imtihon)
class Malakaviy_imtihonAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at', 'updated_at', 'order',)
    search_fields = ('title',)
    fields = ('title_uz', 'title_en', 'content_uz', 'content_en', 'file', 'order',)


@admin.register(Doktarantura)
class DoktaranturaAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at', 'updated_at', 'order',)
    search_fields = ('title',)
    fields = ('title_uz', 'title_en', 'full_name_uz', 'full_name_en', 'labor_activity_uz', 'labor_activity_en',
              'scientific_activity_uz', 'scientific_activity_en', 'works_uz', 'works_en', 'file', 'order')

