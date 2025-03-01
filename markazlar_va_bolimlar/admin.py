from django.contrib import admin
from .models import Xodimlar, Markazlar, Bolimlar, Tadqiqot, Audio, Audiolar, Rasm, Rasmlar, Video, Videolar


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
    fields = ['ful_name_uz', 'ful_name_en', 'about_uz', 'about_en', 'image', 'bolimlar', 'markazlar', 'order']


@admin.register(Tadqiqot)
class TadqiqotAdmin(admin.ModelAdmin):
    list_display = ('title', 'order', 'created_at', 'updated_at')
    search_fields = ('title',)
    fields = ('title_uz', 'title_en', 'content_uz', 'content_en', 'image', 'bolimlar', 'markazlar', 'order')


class Audiolaradmin(admin.TabularInline):
    model = Audiolar
    fields = ['audio',]


@admin.register(Audio)
class AudioAdmin(admin.ModelAdmin):
    list_display = ('title', 'audio',)
    search_fields = ('title',)
    inlines = [Audiolaradmin]
    fields = ['title_uz', 'title_en', 'audio', 'image']


class Rasmlaradmin(admin.TabularInline):
    model = Rasmlar
    fields = ['image']


@admin.register(Rasm)
class RasmAdmin(admin.ModelAdmin):
    list_display = ('title', 'image')
    search_fields = ('title',)
    inlines = [Rasmlaradmin]
    fields = ['title_uz', 'title_en', 'image']


class Videolaradmin(admin.TabularInline):
    model = Videolar
    fields = ['video']


@admin.register(Video)
class RasmAdmin(admin.ModelAdmin):
    list_display = ('title', )
    search_fields = ('title',)
    inlines = [Videolaradmin]
    fields = ['title_uz', 'title_en', 'video', 'image', 'link']