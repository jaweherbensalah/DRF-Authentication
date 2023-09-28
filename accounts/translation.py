from .models import Person

from modeltranslation.translator import register,translator, TranslationOptions


# @register(Person)
class PersonTranslationOptions(TranslationOptions):
    fields = ('name', 'surname', 'profession')

translator.register(Person,PersonTranslationOptions)