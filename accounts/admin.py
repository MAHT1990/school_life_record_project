from django.contrib import admin
from .models import *

# Register your models here.

@admin.register(Member)
class MemberAdmin(admin.ModelAdmin):
    list_display = ['id', 'login_id', 'nickname']
    list_display_links = ['login_id', 'nickname']
