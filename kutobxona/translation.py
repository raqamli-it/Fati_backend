from modeltranslation.translator import TranslationOptions
from .models import *
from modeltranslation.decorators import register


@register(Archive)
class ArchiveTranslationOptions(TranslationOptions):
    fields = ('title',)


@register(Requirements)
class RequirementsTranslationOptions(TranslationOptions):
    fields = ('title', 'content', 'sub_content',)


@register(Period_filter)
class Period_filterTranslationOptions(TranslationOptions):
    fields = ('title',)


@register(Abstract)
class AvtoreferatTranslationOptions(TranslationOptions):
    fields = ('title',)


@register(Editorial)
class TahrirchiTranslationOptions(TranslationOptions):
    fields = ('title', 'position', 'degree', 'sphere', 'content',)


@register(Period)
class ArxivSonTranslationOptions(TranslationOptions):
    fields = ('title',)


@register(Books)
class ArchiveTranslationOptions(TranslationOptions):
    fields = ('title',)


@register(archive_documents)
class ArchiveTranslationOptions(TranslationOptions):
    fields = ('title',)


@register(Mat_category)
class ArchiveTranslationOptions(TranslationOptions):
    fields = ('title',)


@register(Year_filter)
class ArchiveTranslationOptions(TranslationOptions):
    fields = ('title',)


@register(Region_filter)
class ArchiveTranslationOptions(TranslationOptions):
    fields = ('title',)


@register(the_press)
class ArchiveTranslationOptions(TranslationOptions):
    fields = ('title',)