from django.core.exceptions import FieldError
from django.shortcuts import render
from phones.models import Phone


def show_catalog(request):
    template = 'catalog.html'
    sort = request.GET.get('sort')
    if sort:
        if sort == 'min_price':
            sort = 'price'
        elif sort == 'max_price':
            sort = '-price'
        phones = Phone.objects.all().order_by(sort)
        try:
            list(phones)
        except FieldError:
            phones = Phone.objects.all()
    else:
        phones = Phone.objects.all()
    context = {'phones': phones}
    return render(request, template, context)


def show_product(request, slug):
    template = 'product.html'
    phone = Phone.objects.get(slug=slug)
    name = phone.name
    context = {'phone': phone}
    return render(request, template, context)
