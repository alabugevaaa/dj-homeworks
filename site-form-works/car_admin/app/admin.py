from django.contrib import admin

from .models import Car, Review
from .forms import ReviewAdminForm


class CarAdmin(admin.ModelAdmin):
    list_display = ('brand', 'model', 'reviews_count')
    list_filter = ('brand', 'model')
    search_fields = ['brand', 'model']

    def reviews_count(self, obj):
        return obj.reviews.count()

    reviews_count.short_description = 'Количество статей'


class ReviewAdmin(admin.ModelAdmin):
    list_display = ('car', 'title')
    list_filter = ('car__brand',)
    search_fields = ['car__brand', 'car__model', 'title']
    form = ReviewAdminForm


admin.site.register(Car, CarAdmin)
admin.site.register(Review, ReviewAdmin)
