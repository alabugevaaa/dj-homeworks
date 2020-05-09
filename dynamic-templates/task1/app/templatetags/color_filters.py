from django import template

register = template.Library()


@register.filter
def color_value(value, idx):
    color = 'white'
    try:
        value = float(value)
    except ValueError:
        return color
    if idx > 1:
        if idx == 14:
            color = 'grey'
        elif value < 0:
            color = 'green'
        elif value > 5:
            color = 'red'
        elif 2 < value <= 5:
            color = '#f98c8c'
        elif 1 < value <= 2:
            color = '#fcd3d3'
    return color
