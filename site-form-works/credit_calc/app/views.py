from django.shortcuts import render

from .forms import CalcForm


def calc_view(request):
    template = "app/calc.html"

    form = CalcForm(request.GET)

    context = {
        'form': form,
    }

    if form.is_valid():
        params = form.clean()
        result = (params['initial_fee'] + params['initial_fee'] * (params['rate']/100)) / params['months_count']
        common_result = result * params['months_count']
        context['result'] = ('%f' % round(result, 2)).rstrip('0').rstrip('.')
        context['common_result'] = ('%f' % round(common_result, 2)).rstrip('0').rstrip('.')

    return render(request, template, context)
