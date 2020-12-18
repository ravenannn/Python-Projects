from django.contrib import admin

from .models import djangoClasses

# register created model
admin.site.register(djangoClasses)
