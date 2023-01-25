from django.contrib import admin
from .models import Profile


class ListUser(admin.ModelAdmin):
   list_display = ('user', 'registration')


admin.site.register(Profile, ListUser)
