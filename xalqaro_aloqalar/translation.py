from modeltranslation.translator import TranslationOptions
from modeltranslation.decorators import register

from xalqaro_aloqalar.models import Xamkor_tashkilot, Xamkor_loihalar, Tadqiqot, Xalqaro_sayohatlar


@register(Xamkor_tashkilot)
class Xamkor_tashkilotTranslationOptions(TranslationOptions):
    fields = ('title', 'content',)


@register(Xamkor_loihalar)
class Xamkor_loihalarTranslationOptions(TranslationOptions):
    fields = ('title', 'content',)


@register(Tadqiqot)
class Xalqaro_tadqiqotTranslationOptions(TranslationOptions):
    fields = ('title', 'content',)


@register(Xalqaro_sayohatlar)
class Xalqaro_sayohatlarTranslationOptions(TranslationOptions):
    fields = ('title', 'content', 'subcontent',)
