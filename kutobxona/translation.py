from modeltranslation.translator import TranslationOptions
from .models import Avtoreferat, Category, Tahririyat, Arxiv, Talablar
from modeltranslation.decorators import register


@register(Arxiv)
class ArchiveTranslationOptions(TranslationOptions):
    fields = ('title', 'content',)


@register(Talablar)
class RequirementsTranslationOptions(TranslationOptions):
    fields = ('title', 'content', 'sub_content',)


@register(Avtoreferat)
class AvtoreferatTranslationOptions(TranslationOptions):
    fields = ('title', 'content')


@register(Tahririyat)
class TahrirchiTranslationOptions(TranslationOptions):
    fields = ('title', 'position', 'degree', 'sphere', 'content',)


@register(Category)
class ArxivSonTranslationOptions(TranslationOptions):
    fields = ('title',)