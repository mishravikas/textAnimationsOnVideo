from django.contrib import admin

# Register your models here.

from .models import Animation, Video

admin.site.register(Video)
admin.site.register(Animation)
