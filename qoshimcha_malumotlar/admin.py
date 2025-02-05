from django.contrib import admin

from .models import Institut_tarixi, Aloqa, Karusel, Rahbariyat, \
    Tashkiliy_tuzulma, Yangiliklar, Havolalar, Direktorlar, Xabarlar


class Derektorlaradmin(admin.TabularInline):
    model = Direktorlar
    fields = ['title_uz', 'title_en', 'image']


@admin.register(Institut_tarixi)
class Institut_tarixiAdmin(admin.ModelAdmin):
    list_display = ('title', 'status', 'created_at', 'updated_at', 'order',)
    search_fields = ('title',)
    inlines = [Derektorlaradmin]
    fields = ['title_uz', 'title_en', 'content_uz', 'content_en', 'image', 'status', 'order',]


@admin.register(Aloqa)
class AloqaAdmin(admin.ModelAdmin):
    list_display = ('phone', 'email', 'status', 'created_at', 'updated_at', 'order',)
    search_fields = ('title',)
    fields = ('phone', 'email', 'adress', 'lat', 'long', 'youtube', 'telegram', 'instagram',
              'facebook', 'status', 'order', )


@admin.register(Karusel)
class KaruselAdmin(admin.ModelAdmin):
    fields = ['file', 'link', ]


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
    fields = ['title_uz', 'title_en', 'content_uz', 'content_en',  'image',
              'status', 'order']


@admin.register(Havolalar)
class HavolalarAdmin(admin.ModelAdmin):
    list_display = ('title', 'status', 'created_at', 'updated_at', 'order',)
    search_fields = ('title',)
    fields = ['title_uz', 'title_en', 'file', 'link', 'status', 'order',]


@admin.register(Xabarlar)
class XabarlarAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone', 'content')  # Admin panelda ko'rinishi
    search_fields = ('name', 'phone')  # Qidiruv