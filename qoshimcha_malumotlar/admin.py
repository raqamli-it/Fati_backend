from django.contrib import admin

from .models import Institut_tarixi, Aloqa, Karusel, Rahbariyat, \
    Tashkiliy_tuzulma, Yangiliklar, Havolalar, Xabarlar, Category, Kadirlar_bolim, Xodimlar_turlari, Xodimlar


@admin.register(Xodimlar_turlari)
class XodimlarTurlariAdmin(admin.ModelAdmin):
    list_display = ('title', 'order')
    search_fields = ('title',)
    fields = ['title_uz', 'title_en', 'order']


@admin.register(Xodimlar)
class XodimlarAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'category', 'order')
    search_fields = ('full_name',)
    fields = ('full_name', 'year', 'image', 'category', 'order')
    list_filter = ['category']


@admin.register(Institut_tarixi)
class Institut_tarixiAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at', 'updated_at', 'order',)
    search_fields = ('title',)
    fields = ['title_uz', 'title_en', 'content_uz', 'content_en', 'image', 'order',]


@admin.register(Aloqa)
class AloqaAdmin(admin.ModelAdmin):
    list_display = ('phone', 'email', 'created_at', 'updated_at', )
    search_fields = ('title',)
    fields = ('phone', 'email', 'adress', 'lat', 'long', 'youtube', 'telegram', 'instagram', 'facebook',)


@admin.register(Karusel)
class KaruselAdmin(admin.ModelAdmin):
    fields = ['file', 'link', ]


@admin.register(Rahbariyat)
class RahbariyatAdmin(admin.ModelAdmin):
    list_display = ('title', 'position', 'created_at', 'updated_at', 'order',)
    search_fields = ('title',)
    fields = ['title_uz', 'title_en', 'position_uz', 'position_en', 'degree_uz', 'degree_en', 'contact', 'days',
              'image', 'order',]


@admin.register(Tashkiliy_tuzulma)
class Tashkiliy_tuzulmaAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at', 'updated_at', 'order',)
    search_fields = ('title',)
    fields = ['title_uz', 'title_en', 'content_uz', 'content_en', 'file', 'order',]


@admin.register(Yangiliklar)
class YangiliklarAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at', 'updated_at', 'order',)
    search_fields = ('title',)
    fields = ['title_uz', 'title_en', 'content_uz', 'content_en', 'image', 'link', 'order', 'created_at']


@admin.register(Havolalar)
class HavolalarAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at', 'updated_at', 'order',)
    search_fields = ('title',)
    fields = ['title_uz', 'title_en', 'file', 'link', 'order',]


@admin.register(Xabarlar)
class XabarlarAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone', 'content')  # Admin panelda ko'rinishi
    search_fields = ('name', 'phone')  # Qidiruv


@admin.register(Kadirlar_bolim)
class kadirlar_bolimiAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'position',)
    search_fields = ('full_name',)
    fields = ('full_name', 'position', 'image', 'category')
    list_filter = ['category']


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title',)
    fields = ['title']


