from django.contrib import admin
from .models import User, UserProfile
from django.contrib.auth.admin import UserAdmin

class CustomAdmin(UserAdmin):
    ordering=('-date_joined',)
    filter_horizontal=()
    fieldsets=()
    list_filter=()

# Register your models here.
admin.site.register(User,CustomAdmin)
admin.site.register(UserProfile)