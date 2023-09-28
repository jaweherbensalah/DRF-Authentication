from django.contrib import admin
from .models import *
from modeltranslation.admin import TranslationAdmin


@admin.register(Post)
class PostAdmin(TranslationAdmin):
    list_display=['title']

@admin.register(TranslationTest)
class PostAdmin(admin.ModelAdmin):
    list_display=['title']
