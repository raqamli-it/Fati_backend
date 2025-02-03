from modeltranslation.translator import TranslationOptions
from modeltranslation.decorators import register
from .models import Ilmiy_kengash_majlis, Yosh_olimlar
from .models import Azolar


@register(Ilmiy_kengash_majlis)
class Ilmiy_kengash_majlisTranslationOptions(TranslationOptions):
    fields = ('title', 'content',)


@register(Yosh_olimlar)
class Yosh_olimlarTranslationOptions(TranslationOptions):
    fields = ('title', 'content', )


@register(Azolar)
class DissertatsiyaIshlarTranslationOptions(TranslationOptions):
    fields = ('name', 'position', 'degree', )

