from django.contrib import admin
from phones.models import Phone


class PhoneAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}


admin.site.register(Phone, PhoneAdmin)