from modeltranslation.translator import TranslationOptions
from .models import Avtoreferat, Manba, Tahrirchi, ElektronKitob,Arxiv
from modeltranslation.decorators import register
from .models import Talablar


@register(Arxiv)
class ArchiveTranslationOptions(TranslationOptions):
    fields = ('title', 'content',)


@register(Talablar)
class RequirementsTranslationOptions(TranslationOptions):
    fields = ('title', 'content',)


@register(Avtoreferat)
class AvtoreferatTranslationOptions(TranslationOptions):
    fields = ('title',)


@register(Manba)
class ManbaTranslationOptions(TranslationOptions):
    fields = ('title',)


@register(Tahrirchi)
class TahrirchiTranslationOptions(TranslationOptions):
    fields = ('title',)


@register(ElektronKitob)
class ArxivSonTranslationOptions(TranslationOptions):
    fields = ('title',)