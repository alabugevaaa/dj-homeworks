from django.contrib import admin
from django.core.exceptions import ValidationError
from django.forms import BaseInlineFormSet

from .models import Article, Articleship, Subject


class ArticleshipInlineFormset(BaseInlineFormSet):
    def clean(self):
        count_true = 0
        for form in self.forms:
            if form.cleaned_data.get('is_main'):
                count_true += 1
                if count_true > 1:
                    raise ValidationError('Основным может быть только один раздел')
        if count_true == 0:
            raise ValidationError('Укажите основной раздел')
        return super().clean()  # вызываем базовый код переопределяемого метода


class ArticleshipInline(admin.TabularInline):
    model = Articleship
    formset = ArticleshipInlineFormset


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    inlines = [ArticleshipInline]


@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    pass
