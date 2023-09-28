from django.contrib import admin
from .models import Person
from modeltranslation.admin import TranslationAdmin

class PersonAdmin(TranslationAdmin):
    pass

admin.site.register(Person)