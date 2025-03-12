from modeltranslation.translator import TranslationOptions
from .models import *
from modeltranslation.decorators import register


@register(Archive)
class ArchiveTranslationOptions(TranslationOptions):
    fields = ('title',)


@register(Requirements)
class RequirementsTranslationOptions(TranslationOptions):
    fields = ('title', 'content', 'sub_content',)


@register(Abstract)
class AvtoreferatTranslationOptions(TranslationOptions):
    fields = ('title', 'title_two')


@register(Editorial)
class TahrirchiTranslationOptions(TranslationOptions):
    fields = ('title', 'content',)


@register(Sources)
class SourcesTranslationOptions(TranslationOptions):
    fields = ('title', 'title_two')


@register(Literature)
class LiteratureTranslationOptions(TranslationOptions):
    fields = ('title', 'title_two')
