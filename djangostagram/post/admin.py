from django.contrib import admin
from .models import Post


class PostAdmin(admin.ModelAdmin):
    list_display =  ('writer','contents')

admin.site.register(Post, PostAdmin)

