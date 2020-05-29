from django import forms

from .widgets import AjaxInputWidget
from .models import City


class SearchTicket(forms.Form):
    city_from = forms.CharField(label="Город отправления",
                                widget=AjaxInputWidget('api/city_ajax', attrs={'class': 'inline right-margin'}))
    city_to = forms.ModelChoiceField(label="Город прибытия",
                                     queryset=City.objects.all())
    date = forms.DateField(label="Дата",
                           widget=forms.SelectDateWidget)
