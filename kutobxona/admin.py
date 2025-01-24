
from .models import Tahririyat, Avtoreferat, Talablar, Category, Arxiv
from django.contrib import admin


@admin.register(Talablar)
class RequirementsAdmin(admin.ModelAdmin):
    list_display = ('title', 'status', 'created_at', 'Updated_at', 'order',)
    search_fields = ('title',)
    fields = ('title_uz', 'title_en', 'content_uz', 'content_en', 'sub_content_uz', 'sub_content_en',
              'image', 'status', 'order',)


@admin.register(Tahririyat)
class TahririyatAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at', 'Updated_at', 'order',)
    search_fields = ('title',)
    fields = ['title_uz', 'title_en', 'position_uz', 'position_en', 'degree_uz', 'degree_en', 'sphere_uz', 'sphere_en',
              'email', 'content_uz', 'content_en', 'file', 'status', 'order',]


@admin.register(Avtoreferat)
class AvtoreferatAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at', 'Updated_at', 'order',)
    search_fields = ('title',)
    fields = ['title_uz', 'title_en', 'image', 'file', 'content_uz', 'content_en', 'status', 'order', 'category']


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at', 'updated_at', 'order',)
    search_fields = ('title',)
    fields = ['title_uz', 'title_en', 'status', 'order',]


@admin.register(Arxiv)
class ArxivAdmin(admin.ModelAdmin):
    list_display = ('title', 'status', 'order', 'created_at', 'Updated_at')
    search_fields = ('title',)
    fields = ['title_uz', 'title_en', 'content_uz', 'content_en', 'sub_content_uz', 'sub_content_en',
              'image', 'status', 'order',]

