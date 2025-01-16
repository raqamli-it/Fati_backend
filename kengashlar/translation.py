from modeltranslation.translator import TranslationOptions
from modeltranslation.decorators import register
from kengashlar.models import Ilmiy_kengash_majlis, fon_picture, Yosh_olimlar
from kengashlar.models import Azolar


@register(fon_picture)
class fon_pictureTranslationOptions(TranslationOptions):
    fields = ('title', 'content', )
#


@register(Ilmiy_kengash_majlis)
class Ilmiy_kengash_majlisTranslationOptions(TranslationOptions):
    fields = ('title', 'content',)


@register(Yosh_olimlar)
class Yosh_olimlarTranslationOptions(TranslationOptions):
    fields = ('title', 'content', )


@register(Azolar)
class DissertatsiyaIshlarTranslationOptions(TranslationOptions):
    fields = ('name', 'ish_joy', 'lavozim', 'ilmiy_darajasi', 'ilmiy_unvoni')

#
# @register(DissertatsiyaIshlar)
# class AzolarTranslationOptions(TranslationOptions):
#     fields = ('title', 'content')


# @register(Content)
# class contentTranslationOptions(TranslationOptions):
#     fields = ('content',)
