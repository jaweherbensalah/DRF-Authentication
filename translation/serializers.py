from django.contrib.auth.models import User, Group
from rest_framework import serializers
from .models import Post, TranslationTest
from django.utils.translation import gettext_lazy as _

# class TranslatedCharField(serializers.CharField):
#     def get_field_names(self, declared_fields, info):
#         field_names = super().get_field_names(declared_fields, info)
#         translated_field_names = [str(_('title')).lower() if field_name == 'title' else field_name for field_name in field_names]
#         return translated_field_names
class TranslationFieldMixin(object):
    def get_field_names(self, *args, **kwargs):
        field_names = super().get_field_names(*args, **kwargs)
        translated_field_names = [
            str(_('about'))
           
        ]
        return translated_field_names
class PostSerializer(TranslationFieldMixin, serializers.ModelSerializer):
    # title = TranslatedCharField()
    class Meta:
        model = Post
        fields = ['title','about']



class TranslationTestSerializer(TranslationFieldMixin,serializers.ModelSerializer):

    class Meta:
        model = TranslationTest
        fields = ['title','about']