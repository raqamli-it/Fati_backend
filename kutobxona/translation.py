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
    fields = ('title',)


@register(Editorial)
class TahrirchiTranslationOptions(TranslationOptions):
    fields = ('title', 'position', 'degree', 'sphere', 'content',)


@register(Sources)
class SourcesTranslationOptions(TranslationOptions):
    fields = ('title',)


@register(Literature)
class LiteratureTranslationOptions(TranslationOptions):
    fields = ('title',)
#
#
# @register(Archive_documents)
# class ArchiveTranslationOptions(TranslationOptions):
#     fields = ('title',)