from django.contrib import admin
from .models import WaypointFile


@admin.register(WaypointFile)
class WaypointFileAdmin(admin.ModelAdmin):
    list_display = [field.name for field in WaypointFile._meta.fields]
    ordering = ['id']
    list_display_links = ['id']
