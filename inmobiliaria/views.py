from django.shortcuts import render
from .models import Property

def properties(request):
    property_type = request.GET.get('property_type')
    if property_type:
        title = property_type
        properties = Property.objects.filter(property_type=property_type)
    else:
        title = 'Propiedades'
        properties = Property.objects.all()
    context = {'title': title, 'properties': properties}
    return render(request, 'inmobiliaria/properties.html', context)