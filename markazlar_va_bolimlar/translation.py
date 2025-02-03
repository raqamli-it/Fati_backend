from modeltranslation.translator import TranslationOptions
from modeltranslation.decorators import register
from .models import Xodimlar, Markazlar_Bolimlar, Tadqiqot, Video, Photo


@register(Markazlar_Bolimlar)
class Markazlar_bolimlarTranslationOptions(TranslationOptions):
    fields = ('title', 'content',)


@register(Tadqiqot)
class TadqiqotTranslationOptions(TranslationOptions):
    fields = ('title', 'content',)


@register(Xodimlar)
class XodimlarTranslationOptions(TranslationOptions):
    fields = ('title', 'sphere', 'position', 'academic_degree', 'about', 'works')


@register(Video)
class VideoTranslationOptions(TranslationOptions):
    fields = ('title',)


@register(Photo)
class RasmTranslationOptions(TranslationOptions):
    fields = ('title',)