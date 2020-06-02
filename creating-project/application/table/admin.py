from django.contrib import admin
from .models import Table, Path


class TableAdmin(admin.ModelAdmin):
    pass


class PathAdmin(admin.ModelAdmin):
    pass


admin.site.register(Table, TableAdmin)
admin.site.register(Path, PathAdmin)
