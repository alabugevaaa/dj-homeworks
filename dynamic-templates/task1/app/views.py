import csv
from django.shortcuts import render


def inflation_view(request):
    template_name = 'inflation.html'

    # чтение csv-файла и заполнение контекста
    with open('inflation_russia.csv', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile, delimiter=';')
        years = list(reader)[1:]
    context = {'years': years}

    return render(request, template_name,
                  context)
