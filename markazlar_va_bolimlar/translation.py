from modeltranslation.translator import TranslationOptions
from modeltranslation.decorators import register
from markazlar_va_bolimlar.models import Xodimlar, MarkazlarBolimlar


@register(Xodimlar)
class XodimlarTranslationOptions(TranslationOptions):
    fields = ('name', 'lavozim', 'ilmiy_daraja')


@register(MarkazlarBolimlar)
class MarkazlarBolimlarTranslationOptions(TranslationOptions):
    fields = ('tarix', 'title')