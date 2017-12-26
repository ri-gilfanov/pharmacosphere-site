from django.contrib import admin
from .models import CustomPage
from mptt.admin import DraggableMPTTAdmin


@admin.register(CustomPage)
class CustomPageAdmin(DraggableMPTTAdmin):
    pass
