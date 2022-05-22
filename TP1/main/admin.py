from django.contrib import admin
from .models import Post
from .models import Reply

# Register your models here.

admin.site.register(Post)
admin.site.register(Reply)