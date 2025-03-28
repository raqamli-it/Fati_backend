from modeltranslation.translator import TranslationOptions
from modeltranslation.decorators import register
from .models import Xodimlar, Markazlar, Bolimlar, Tadqiqot, Video, Rasm, Audio


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
    fields = ('full_name', 'about', 'degree', 'position', 'works', 'surname')


@register(Video)
class VideoTranslationOptions(TranslationOptions):
    fields = ['title']


@register(Rasm)
class RasmTranslationOptions(TranslationOptions):
    fields = ['title']


@register(Audio)
class AudioTranslationOptions(TranslationOptions):
    fields = ['title']