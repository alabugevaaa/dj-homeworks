from django.contrib import admin
from stations.models import Route, Station


class StationAdmin(admin.ModelAdmin):
    pass


class RouteAdmin(admin.ModelAdmin):
    pass


admin.site.register(Station, StationAdmin)
admin.site.register(Route, RouteAdmin)
