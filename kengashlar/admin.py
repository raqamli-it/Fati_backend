from .models import Ilmiy_kengash_majlis, Yosh_olimlar
from django.contrib import admin
from .models import Azolar, Elonlar, Xodimlar, Kadirlar


class Xodimlaradmin(admin.TabularInline):
    model = Xodimlar
    fields = ('full_name_uz', 'full_name_en', 'image')  # Only include fields that exist in the model


@admin.register(Ilmiy_kengash_majlis)
class Ilmiy_kengash_majlisAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at', 'updated_at',)
    search_fields = ('title',)
    inlines = [Xodimlaradmin]
    fields = ('title_uz', 'title_en', 'content_uz', 'content_en',)


@admin.register(Yosh_olimlar)
class Yosh_olimlarAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at', 'updated_at',)
    search_fields = ('title',)
    fields = ('title_uz', 'title_en', 'content_uz', 'content_en', 'file',)


class Kadirlaradmin(admin.TabularInline):
    model = Kadirlar
    fields = ['full_name_uz', 'full_name_en', 'image', 'workplace_uz', 'workplace_en', 'position_uz', 'position_en',
              'shifri', 'degree_uz', 'degree_en', 'academic_title_uz', 'academic_title_en',]


@admin.register(Azolar)
class AzolarAdmin(admin.ModelAdmin):
    list_display = ['title', 'created_at', 'updated_at',]
    search_fields = ('title',)
    inlines = [Kadirlaradmin]
    fields = ['title_uz', 'title_en', 'content_uz', 'content_en',]


@admin.register(Elonlar)
class ElonlarAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at', 'updated_at',)
    search_fields = ('title',)
    fields = ['title_uz', 'title_en', 'content_uz', 'content_en', 'image']