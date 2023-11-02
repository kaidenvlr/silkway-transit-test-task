from django.contrib import admin

from main.models import LocomotivePart


@admin.register(LocomotivePart)
class LocomotivePartAdmin(admin.ModelAdmin):
    list_display = ['id', 'schema_id', 'parent']
    search_fields = ['schema_id']
    list_per_page = 10
    ordering = ('id',)
