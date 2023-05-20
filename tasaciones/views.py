from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings
from .forms import TasacionForm


def tasacion(request):
    form = TasacionForm(request.POST or None, request.FILES or None)

    if request.method == 'POST':
        if form.is_valid():
            tasacion = form.save()

            # Envíe un correo electrónico con los detalles de la tasación.
            send_mail(
                'Nueva tasación',
                f"Se ha enviado una nueva solicitud de tasación. Por favor, revise el panel de administración para ver los detalles.",
                settings.EMAIL_HOST_USER,
                [settings.EMAIL_HOST_USER],
                fail_silently=False,
            )
            return render(request, 'tasaciones/success.html')

    return render(request, 'tasaciones/solicitar_tasacion.html', {'form': form})
