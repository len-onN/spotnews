from django.contrib import admin
from .models import User, Category, News

# Register your models here.
admin.site.register(Category)
admin.site.register(User)
admin.site.register(News)
