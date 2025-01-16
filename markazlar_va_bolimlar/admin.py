
from django.contrib import admin
from .models import Xodimlar, MarkazlarBolimlar, Rasmlar


class RasmlarTabularInline(admin.TabularInline):
    model = Rasmlar
    fields = ['silder', 'fotogalereya',]


@admin.register(MarkazlarBolimlar)
class MarkazlarBolimlarTabularInline(admin.ModelAdmin):
    list_display = ('title', 'status', 'order', 'created_at', 'updated_at',)
    inlines = [RasmlarTabularInline]
    fields = ['title_uz', 'title_en', 'tarix_uz', 'tarix_en', 'status', 'order']


@admin.register(Xodimlar)
class XodimlarAdmin(admin.ModelAdmin):
    list_display = ('name', 'lavozim', 'ilmiy_daraja', 'status', 'order', 'created_at', 'updated_at')
    search_fields = ('name',)
    fields = ('name_uz', 'name_en', 'lavozim_uz', 'lavozim_en', 'ilmiy_daraja_uz', 'ilmiy_daraja_en',
              'markazlar_bolimlar', 'status', 'order')

