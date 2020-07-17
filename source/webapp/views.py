from django.shortcuts import render

def calculator_view(request):
    if request.method == 'GET':
        return render(request, 'calculator.html')
    elif request.method == 'POST':
        context = {
            'first_number': int(request.POST.get('first_number')),
            'act': request.POST.get('act'),
            'second_number': int(request.POST.get('second_number')),
            'result': 0
        }
        if context['act'] == 'add':
            context['act'] = '+'
            context['result'] = context['first_number'] + context['second_number']
        elif context['act'] == 'subtract':
            context['act'] = '-'
            context['result'] = context['first_number'] - context['second_number']
        elif context['act'] == 'multiply':
            context['act'] = '*'
            context['result'] = context['first_number'] * context['second_number']
        else:
            context['act'] = '/'
            context['result'] = context['first_number'] / context['second_number']

        return render(request, 'result.html', context)
