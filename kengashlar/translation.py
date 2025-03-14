from modeltranslation.translator import TranslationOptions
from modeltranslation.decorators import register
from .models import Ilmiy_kengash_majlis, Yosh_olimlar, Xodimlar, Kadirlar
from .models import Azolar, Elonlar


@register(Ilmiy_kengash_majlis)
class Ilmiy_kengash_majlisTranslationOptions(TranslationOptions):
    fields = ('title', 'content',)


@register(Yosh_olimlar)
class Yosh_olimlarTranslationOptions(TranslationOptions):
    fields = ('title', 'content',)


@register(Azolar)
class AzolarTranslationOptions(TranslationOptions):
    fields = ('title', 'content',)


@register(Elonlar)
class ElonlarTranslationOptions(TranslationOptions):
    fields = ('title', 'content',)


@register(Xodimlar)
class XodimlarTranslationOptions(TranslationOptions):
    fields = ('full_name', 'position')


@register(Kadirlar)
class KadirlarTranslationOptions(TranslationOptions):
    fields = ('full_name', 'position', 'degree', 'academic_title', 'workplace',)




