import csv

from django.shortcuts import render
from .models import Table, Path


def table_view(request):
    template = 'table.html'
    columns = []
    table = Table.objects.all()
    for column in table:
        col = {'name': column.name,
               'width': column.width}
        columns.append(col)

    path_file = Path.objects.first()
    path = path_file.get_path()
    with open(path, 'rt') as csv_file:
        header = []
        table = []
        table_reader = csv.reader(csv_file, delimiter=';')
        for table_row in table_reader:
            if not header:
                header = {idx: value for idx, value in enumerate(table_row)}
            else:
                row = {header.get(idx) or 'col{:03d}'.format(idx): value
                       for idx, value in enumerate(table_row)}
                table.append(row)

        context = {
            'columns': columns,
            'table': table,
            'csv_file': path
        }
        result = render(request, template, context)
    return result
