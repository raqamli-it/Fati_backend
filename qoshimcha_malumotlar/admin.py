from django.contrib import admin

from qoshimcha_malumotlar.models import Institut_tarixi, Aloqa, Karusel, Rahbariyat, \
    Tashkiliy_tuzulma, Yangiliklar, Havolalar, picture, Kengash_rasm


@admin.register(Institut_tarixi)
class Institut_tarixiAdmin(admin.ModelAdmin):
    list_display = ('title', 'status', 'created_at', 'updated_at', 'order',)
    search_fields = ('title',)
    fields = ['title_uz', 'title_en', 'content_uz', 'content_en', 'subcontent_uz', 'subcontent_en', 'file', 'base_file',
              'status', 'order',]


@admin.register(Aloqa)
class AloqaAdmin(admin.ModelAdmin):
    list_display = ('phone', 'email', 'status', 'created_at', 'updated_at', 'order',)
    search_fields = ('title',)
    fields = ('faks', 'email', 'phone', 'adress', 'lat', 'long', 'youtube', 'telegram', 'instagram',
              'facebook', 'status', 'order', )


@admin.register(Karusel)
class KaruselAdmin(admin.ModelAdmin):
    fields = ['file', 'link', ]


@admin.register(Kengash_rasm)
class kengash_rasmAdmin(admin.ModelAdmin):
    fields = ['title_uz', 'title_en', 'content_uz', 'content_en', 'picture',]


@admin.register(Rahbariyat)
class RahbariyatAdmin(admin.ModelAdmin):
    list_display = ('title', 'position', 'status', 'created_at', 'updated_at', 'order',)
    search_fields = ('title',)
    fields = ['title_uz', 'title_en', 'position_uz', 'position_en', 'degree_uz', 'degree_en', 'contact', 'days',
              'image', 'status', 'order',]


@admin.register(Tashkiliy_tuzulma)
class Tashkiliy_tuzulmaAdmin(admin.ModelAdmin):
    list_display = ('title', 'status', 'created_at', 'updated_at', 'order',)
    search_fields = ('title',)
    fields = ['title_uz', 'title_en', 'content_uz', 'content_en', 'file', 'order', 'status',]


@admin.register(Yangiliklar)
class YangiliklarAdmin(admin.ModelAdmin):
    list_display = ('title', 'status', 'created_at', 'updated_at', 'order',)
    search_fields = ('title',)
    fields = ['title_uz', 'title_en', 'content_uz', 'content_en', 'subcontent_uz', 'subcontent_en', 'file',
              'status', 'order']


@admin.register(Havolalar)
class HavolalarAdmin(admin.ModelAdmin):
    list_display = ('title', 'status', 'created_at', 'updated_at', 'order',)
    search_fields = ('title',)
    fields = ['title_uz', 'title_en', 'file', 'link', 'status', 'order',]


admin.site.register(picture)