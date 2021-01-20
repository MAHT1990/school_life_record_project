from django.contrib import admin
from .models import *
# Register your models here.

@admin.register(Sentence)
class SentenceAdmin(admin.ModelAdmin):
    list_display = ['id', 'content', 'like_count', 'unlike_count']
    list_display_links = ['id', 'content']
