from django.contrib import admin # type: ignore
from .models import Category, Job, Information

admin.site.register(Category)
admin.site.register(Job)
admin.site.register(Information)
        