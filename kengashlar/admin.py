from .models import fon_picture, Ilmiy_kengash_majlis, Yosh_olimlar
from django.contrib import admin
from .models import Azolar


@admin.register(fon_picture)
class fon_pictureAdmin(admin.ModelAdmin):
    list_display = ('title', 'status', 'created_at', 'updated_at', 'order',)
    search_fields = ('title',)
    fields = ('title_uz', 'title_en', 'content_uz', 'content_en', 'file', 'status', 'order',)


@admin.register(Ilmiy_kengash_majlis)
class Ilmiy_kengash_majlisAdmin(admin.ModelAdmin):
    list_display = ('title', 'status', 'created_at', 'updated_at', 'order',)
    search_fields = ('title',)
    fields = ('title_uz', 'title_en', 'content_uz', 'content_en', 'file', 'date', 'status', 'order',)


@admin.register(Yosh_olimlar)
class Yosh_olimlarAdmin(admin.ModelAdmin):
    list_display = ('title', 'status', 'created_at', 'updated_at', 'order',)
    search_fields = ('title',)
    fields = ('title_uz', 'title_en', 'content_uz', 'content_en', 'file', 'status', 'order',)


@admin.register(Azolar)
class AzolarAdmin(admin.ModelAdmin):
    list_display = ['name', 'shifr', 'ish_joy', 'lavozim', 'created_at', 'updated_at', 'order',]
    search_fields = ('name',)
    fields = ['name_uz', 'name_en', 'shifr', 'ish_joy_uz', 'ish_joy_en', 'lavozim_uz', 'lavozim_en',
              'ilmiy_darajasi_uz', 'ilmiy_darajasi_en', 'ilmiy_unvoni_uz', 'ilmiy_unvoni_en', 'status', 'order',]

