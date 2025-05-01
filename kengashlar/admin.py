from .models import Ilmiy_kengash_majlis, Yosh_olimlar, YoshXodim
from django.contrib import admin
from .models import Azolar, Elonlar, Xodimlar, Kadirlar, Text, Content


class TextAdmin(admin.TabularInline):
    model = Text
    extra = 1
    fields = ('content_uz', 'content_en',)


class ContentAdmin(admin.TabularInline):
    model = Content
    extra = 1
    fields = ('content_uz', 'content_en',)


class XodimlarAdmin(admin.TabularInline):
    model = Xodimlar
    fields = ('full_name_uz', 'full_name_en', 'position_uz', 'position_en', 'image')


@admin.register(Ilmiy_kengash_majlis)
class Ilmiy_kengash_majlisAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at', 'updated_at',)
    search_fields = ('title',)
    inlines = [XodimlarAdmin, ContentAdmin]
    fields = ('title_uz', 'title_en', 'content_uz', 'content_en',)


# @admin.register(Yosh_olimlar)
# class Yosh_olimlarAdmin(admin.ModelAdmin):
#     list_display = ('title', 'created_at', 'updated_at',)
#     search_fields = ('title',)
#     fields = ('title_uz', 'title_en', 'content_uz', 'content_en', 'file',)

class XodimInline(admin.TabularInline):
    model = YoshXodim
    extra = 1  # yangi qator qo'shish uchun 1 ta bo'sh joy

@admin.register(Yosh_olimlar)
class Yosh_olimlarAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at', 'updated_at',)
    search_fields = ('title',)
    fields = ('title', 'content', 'file',)  # E'tibor bering, modelda title_uz yo'q edi.
    inlines = [XodimInline]

class Kadirlaradmin(admin.TabularInline):
    model = Kadirlar
    fields = ['full_name_uz', 'full_name_en', 'image', 'workplace_uz', 'workplace_en', 'position_uz', 'position_en',
              'shifri', 'degree_uz', 'degree_en', 'academic_title_uz', 'academic_title_en',]


@admin.register(Azolar)
class AzolarAdmin(admin.ModelAdmin):
    list_display = [ 'fullname', 'title', 'created_at', 'updated_at',]
    search_fields = ('title',)
    inlines = [Kadirlaradmin, TextAdmin]
    fields = ['title_uz', 'title_en', 'content_uz', 'content_en',]


@admin.register(Elonlar)
class ElonlarAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at', 'updated_at', 'order')
    search_fields = ('title',)
    fields = ['title_uz', 'title_en', 'content_uz', 'content_en', 'image', 'order']
