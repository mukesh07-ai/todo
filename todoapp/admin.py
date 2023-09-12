from django.contrib import admin
from .models import *

admin.site.register(todo)

class todoadmin(admin.ModelAdmin):
    list_display = ('topic', 'venue','slot')

# Register your models here.
