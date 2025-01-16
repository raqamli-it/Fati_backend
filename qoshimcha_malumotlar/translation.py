from modeltranslation.translator import TranslationOptions
from modeltranslation.decorators import register
from .models import *


@register(Institut_tarixi)
class Institut_tarixiTranslationOptions(TranslationOptions):
    fields = ('title', 'content', 'subcontent')


@register(Rahbariyat)
class RahbariyatTranslationOptions(TranslationOptions):
    fields = ('title', 'position', 'degree',)


@register(Tashkiliy_tuzulma)
class Tashkiliy_tuzulmaTranslationOptions(TranslationOptions):
    fields = ('title', 'content',)


@register(Yangiliklar)
class YangiliklarTranslationOptions(TranslationOptions):
    fields = ('title', 'content', 'subcontent',)


@register(Havolalar)
class HavolalarTranslationOptions(TranslationOptions):
    fields = ('title',)


@register(Kengash_rasm)
class HavolalarTranslationOptions(TranslationOptions):
    fields = ('title', 'content')


