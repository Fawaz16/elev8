from django.contrib import admin
from .models import Topic, Comment, content_post
# from.models import Header
# Register your models here.

admin.site.register(Topic),
admin.site.register(content_post),
admin.site.register(Comment),
