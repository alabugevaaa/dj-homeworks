from collections import Counter

from django.shortcuts import render_to_response

# Для отладки механизма ab-тестирования используйте эти счетчики
# в качестве хранилища количества показов и количества переходов.
# но помните, что в реальных проектах так не стоит делать
# так как при перезапуске приложения они обнулятся
counter_show = Counter()
counter_click = Counter()


def add_counter(type_counter, param):
    counter = counter_show if type_counter == 'show' else counter_click
    if counter.get(param):
        counter[param] += 1
    else:
        counter[param] = 1
    return counter[param]


def index(request):
    # Реализуйте логику подсчета количества переходов с лендига по GET параметру from-landing
    from_landing = request.GET.get('from-landing')
    if from_landing == 'test':
        add_counter('click', 'test')
    if from_landing == 'original':
        add_counter('click', 'original')
    return render_to_response('index.html')


def landing(request):
    # Реализуйте дополнительное отображение по шаблону app/landing_alternate.html
    # в зависимости от GET параметра ab-test-arg
    # который может принимать значения original и test
    # Так же реализуйте логику подсчета количества показов
    landing = request.GET.get('ab-test-arg', 'original')
    if landing == 'test':
        add_counter('show', 'test')
        return render_to_response('landing_alternate.html')
    else:
        add_counter('show', 'original')
        return render_to_response('landing.html')


def stats(request):
    # Реализуйте логику подсчета отношения количества переходов к количеству показов страницы
    # Чтобы отличить с какой версии лендинга был переход
    # проверяйте GET параметр marker который может принимать значения test и original
    # Для вывода результат передайте в следующем формате:
    test_conversion, original_conversion = 0, 0
    if counter_show['test'] and counter_show['original']:
        test_conversion = counter_click['test'] / counter_show['test']
        original_conversion = counter_click['original'] / counter_show['original']
    return render_to_response('stats.html', context={
        'test_conversion': test_conversion,
        'original_conversion': original_conversion,
    })
