from django.core.mail import send_mail
from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404, redirect

from app.models import Logo
from .forms import VentaForm

from .models import Property, Venta


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





from django.db.models import Q

def search(request):
    search_term = request.GET.get('search_term')
    property_type = request.GET.get('property_type')

    if len(search_term) < 3:
        # Devolver un conjunto de resultados vacío o un mensaje de error
        properties_list = Property.objects.none()
        message = "Por favor, introduce al menos 3 caracteres en tu búsqueda."
    else:
        properties_list = Property.objects.filter(
            Q(title__icontains=search_term) |
            Q(description__icontains=search_term) |
            Q(location__icontains=search_term) |
            Q(property_type__icontains=search_term),
            property_type=property_type
        )
        message = ""

    paginator = Paginator(properties_list, 6)  # Muestra 6 propiedades por página
    page = request.GET.get('page')
    properties = paginator.get_page(page)

    return render(request, 'search_results.html', {'properties': properties, 'search_term': search_term, 'property_type': property_type, 'message': message})


def property_detail(request, property_id):
    property_obj = get_object_or_404(Property, id=property_id)
    return render(request, 'property_detail.html', {'property': property_obj})



def home(request):
    logos = Logo.objects.all()
    return render(request, 'home.html', {'logos': logos})


def venta(request):
    if request.method == 'POST':
        form = VentaForm(request.POST)
        if form.is_valid():
            # Crear una nueva instancia de Venta y guardarla
            venta = Venta()
            venta.nombre = form.cleaned_data['nombre']
            venta.email = form.cleaned_data['email']
            venta.telefono = form.cleaned_data['telefono']
            venta.localidad = form.cleaned_data['localidad']
            venta.provincia = form.cleaned_data['provincia']
            venta.comentarios = form.cleaned_data['comentarios']
            venta.aceptar_terminos = form.cleaned_data['aceptar_terminos']
            venta.save()

            # Enviar correo electrónico
            subject = 'Nuevo registro de venta'
            message = f'Nuevo registro de venta de {venta.nombre}. Comentarios: {venta.comentarios}.'
            send_mail(subject, message, 'your-email@example.com', ['recipient@example.com'])

            return redirect('venta_success')
    else:
        form = VentaForm()

    return render(request, 'inmobiliaria/ventas.html', {'form': form})


def venta_success(request):
    return render(request, 'inmobiliaria/venta_success.html')

