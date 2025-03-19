from django.contrib import admin
from .models import Xodimlar, Markazlar, Bolimlar, Tadqiqot, Audio, Rasm, Rasmlar, Video
from django.utils.html import format_html


@admin.register(Markazlar)
class Markazlaradmin(admin.ModelAdmin):
    list_display = ('title', 'order', 'created_at', 'updated_at')
    search_fields = ('title',)
    fields = ('title_uz', 'title_en', 'content_uz', 'content_en', 'image', 'file', 'order')


@admin.register(Bolimlar)
class Bolimlaradmin(admin.ModelAdmin):
    list_display = ('title', 'order', 'created_at', 'updated_at')
    search_fields = ('title',)
    fields = ('title_uz', 'title_en', 'content_uz', 'content_en', 'image', 'file', 'order')


@admin.register(Xodimlar)
class XodimlarAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'order', 'created_at', 'updated_at')
    search_fields = ('full_name',)
    fields = ['full_name_uz', 'full_name_en', 'surname_uz', 'surname_en', 'position_uz', 'position_en', 'degree_uz', 'degree_en', 'about_uz',
              'about_en', 'image', 'bolimlar', 'markazlar', 'order']
    list_filter = ('bolimlar', 'markazlar')  # Filter qo'shish


@admin.register(Tadqiqot)
class TadqiqotAdmin(admin.ModelAdmin):
    list_display = ('title', 'order', 'created_at', 'updated_at')
    search_fields = ('title',)
    fields = ('title_uz', 'title_en', 'content_uz', 'content_en', 'image', 'bolimlar', 'markazlar', 'order')
    list_filter = ('bolimlar', 'markazlar')


#
# class Audiolaradmin(admin.TabularInline):
#     model = Audiolar
#     fields = ['audio', ]


@admin.register(Audio)
class AudioAdmin(admin.ModelAdmin):
    list_display = ('title', 'get_image', 'get_audio')
    search_fields = ('title',)
    # inlines = [Audiolaradmin]
    fields = ['title_uz', 'title_en', 'audio', 'image', 'order']

    def get_audio(self, obj):
        if obj.audio:
            return format_html(
                '<audio controls><source src="{}" type="audio/mp3">Your browser does not support the audio element.</audio>',
                obj.audio.url)
        return '-'

    get_audio.short_description = 'Audio File'

    def get_image(self, obj):
        if obj.image:
            return format_html('<img src="{}" style="max-width: 60px; max-height: 60px;" />'.format(obj.image.url))
        return '-'

    get_image.short_description = 'Image'


class Rasmlaradmin(admin.TabularInline):
    model = Rasmlar
    fields = ['image']


@admin.register(Rasm)
class RasmAdmin(admin.ModelAdmin):
    list_display = ('title', 'get_image')
    search_fields = ('title',)
    inlines = [Rasmlaradmin]
    fields = ['title_uz', 'title_en', 'image']

    def get_image(self, obj):
        if obj.image:
            return format_html('<img src="{}" style="max-width: 100px; max-height: 100px;" />'.format(obj.image.url))
        return '-'

    get_image.short_description = 'Image'
#
#
# class Videolaradmin(admin.TabularInline):
#     model = Videolar
#     fields = ['video']


@admin.register(Video)
class RasmAdmin(admin.ModelAdmin):
    list_display = ('title', 'get_image')
    search_fields = ('title',)
    # inlines = [Videolaradmin]
    fields = ['title_uz', 'title_en', 'video', 'image', 'link', 'order']

    def get_image(self, obj):
        if obj.image:
            return format_html('<img src="{}" style="max-width: 100px; max-height: 100px;" />'.format(obj.image.url))
        return '-'

    get_image.short_description = 'Image'
