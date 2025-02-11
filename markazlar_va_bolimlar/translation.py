from modeltranslation.translator import TranslationOptions
from modeltranslation.decorators import register
from .models import Xodimlar, Markazlar, Bolimlar, Tadqiqot, Video, Photo


@register(Markazlar)
class Markazlar_bolimlarTranslationOptions(TranslationOptions):
    fields = ('title', 'content',)


@register(Bolimlar)
class Markazlar_bolimlarTranslationOptions(TranslationOptions):
    fields = ('title', 'content',)


@register(Tadqiqot)
class TadqiqotTranslationOptions(TranslationOptions):
    fields = ('title', 'content',)


@register(Xodimlar)
class XodimlarTranslationOptions(TranslationOptions):
    fields = ('ful_name', 'activity', 'about', 'works')


@register(Video)
class VideoTranslationOptions(TranslationOptions):
    fields = ('title',)


@register(Photo)
class RasmTranslationOptions(TranslationOptions):
    fields = ('title',)