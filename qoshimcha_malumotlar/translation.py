from modeltranslation.translator import TranslationOptions
from modeltranslation.decorators import register
from .models import *


@register(Xodimlar_turlari)
class Xodimlar_turlariTranslationOptions(TranslationOptions):
    fields = ('title', )


@register(Xodimlar)
class XodimlarTranslationOptions(TranslationOptions):
    fields = ('full_name',)


@register(Institut_tarixi)
class Institut_tarixiTranslationOptions(TranslationOptions):
    fields = ('title', 'content',)


@register(Rahbariyat)
class RahbariyatTranslationOptions(TranslationOptions):
    fields = ('title', 'position', 'degree', 'description')


@register(Tashkiliy_tuzulma)
class Tashkiliy_tuzulmaTranslationOptions(TranslationOptions):
    fields = ('title', 'content',)


@register(Yangiliklar)
class YangiliklarTranslationOptions(TranslationOptions):
    fields = ('title', 'content', )


@register(Havolalar)
class HavolalarTranslationOptions(TranslationOptions):
    fields = ('title',)

