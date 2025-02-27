from .models import Ilmiy_kengash_majlis, Yosh_olimlar
from django.contrib import admin
from .models import Azolar, Elonlar


@admin.register(Ilmiy_kengash_majlis)
class Ilmiy_kengash_majlisAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at', 'updated_at',)
    search_fields = ('title',)
    fields = ('title_uz', 'title_en', 'content_uz', 'content_en',)


@admin.register(Yosh_olimlar)
class Yosh_olimlarAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at', 'updated_at',)
    search_fields = ('title',)
    fields = ('title_uz', 'title_en', 'content_uz', 'content_en', 'file',)


@admin.register(Azolar)
class AzolarAdmin(admin.ModelAdmin):
    list_display = ['title', 'created_at', 'updated_at',]
    search_fields = ('title',)
    fields = ['title_uz', 'title_en', 'content_uz', 'content_en',]


@admin.register(Elonlar)
class AzolarAdmin(admin.ModelAdmin):
    list_display = ['title', 'created_at', 'updated_at',]
    search_fields = ('title',)
    fields = ['title_uz', 'title_en', 'content_uz', 'content_en', 'image']


