import datetime
import os
from django.conf import settings
from django.shortcuts import render


def file_list(request, date=None):
    template_name = 'index.html'
    date = date.date() if date else None
    files = []
    dir = os.listdir(path=settings.FILES_PATH)
    for f in dir:
        info = os.stat(os.path.join(settings.FILES_PATH, f))
        ctime = datetime.datetime.fromtimestamp(info.st_ctime)
        mtime = datetime.datetime.fromtimestamp(info.st_mtime)
        if (date and (ctime.date() == date or mtime.date() == date)) or not date:
            file = {'name': f,
                    'ctime': ctime,
                    'mtime': mtime}
            files.append(file)

    context = {
        'files': files,
        'date': date
    }

    return render(request, template_name, context)


def file_content(request, name):
    with open(os.path.join(settings.FILES_PATH, name)) as f:
        content = f.read()
    return render(
        request,
        'file_content.html',
        context={'file_name': name, 'file_content': content}
    )

