from django.contrib import admin
from app_name.models  import Category, Post

admin.site.register(Post)
admin.site.register(Category)