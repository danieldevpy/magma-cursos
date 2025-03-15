from django.shortcuts import render
from certificate.models import Certificate


def index(request):
    context = {'certificates': {}}
    certificates = Certificate.objects.all()
    for certificate in certificates:
        if not certificate.model.name in context['certificates']:
            context['certificates'][certificate.model.name] = 0
        context['certificates'][certificate.model.name] += 1
 
    print(context)
    return render(request, 'dash.html', context=context)

def preview(request):
    return render(request, 'preview.html')

def history(request, term=None):
    context = {}
    if term:
        context['term'] = term
        context['certificates'] = [certificate.render_html() for certificate in Certificate.objects.filter(identifier__contains=term)]
    else:
        context['certificates'] = [certificate.render_html() for certificate in Certificate.objects.all()]
    
    return render(request, 'history.html', context=context)
