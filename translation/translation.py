from .models import Post

from modeltranslation.translator import register,translator, TranslationOptions


@register(Post)
class PersonTranslationOptions(TranslationOptions):
    fields = ('title', 'about')
