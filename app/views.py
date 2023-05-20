


from django.shortcuts import render

from inmobiliaria.models import Property


def home(request):
    ultimas_propiedades_vendidas = Property.objects.filter(vendido=True).order_by('-id')[:4]
    ultimas_propiedades_alquiladas = Property.objects.filter(alquilado=True).order_by('-id')[:4]
    context = {'ultimas_propiedades_vendidas': ultimas_propiedades_vendidas,
               'ultimas_propiedades_alquiladas': ultimas_propiedades_alquiladas}
    return render(request, 'home.html', context)



def nosotros(request):
    return render(request, 'nosotros/nosotros.html')
