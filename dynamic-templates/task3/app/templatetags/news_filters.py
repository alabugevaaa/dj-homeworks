from datetime import datetime, timedelta
from django import template


register = template.Library()


@register.filter
def format_date(value):
    now = datetime.now()
    date = datetime.fromtimestamp(value)
    delta = (now - date).seconds
    hours, _ = divmod(delta, 3600)
    if delta < 600:
        return 'только что'
    elif hours < 24:
        return f'{hours} часов назад'
    return date


@register.filter
def format_score(value):
    if not value:
        value = 0
    if value < -5:
        return 'всё плохо'
    elif -5 <= value < 5:
        return 'нейтрально'
    else:
        return 'хорошо'


@register.filter
def format_num_comments(value):
    if value == 0:
        return 'Оставьте комментарий'
    elif value <= 50:
        return value
    else:
        return '50+'


@register.filter
def format_selftext(value, count):
    return f'{value[:count]}...{value[-count:]}'


