from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.conf import settings
from .forms import ContactForm
from .models import Contact

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            email = form.cleaned_data['email']
            inquiry_type = form.cleaned_data['inquiry_type']
            message = form.cleaned_data['message']

            # Guarda la información del contacto en la base de datos
            new_contact = Contact(
                first_name=first_name,
                last_name=last_name,
                email=email,
                inquiry_type=inquiry_type,
                message=message
            )
            new_contact.save()

            # Construye el mensaje del correo electrónico
            email_subject = f'{inquiry_type} - {first_name} {last_name}'
            email_message = f'Nombre: {first_name}\nApellido: {last_name}\nEmail: {email}\nTipo de consulta: {inquiry_type}\nConsulta:\n{message}'

            # Envía el correo electrónico al administrador
            from_email = 'noreply@example.com'
            to_email = [settings.EMAIL_HOST_USER]
            send_mail(email_subject, email_message, from_email, to_email)

            # Envía un correo electrónico de confirmación al usuario
            confirmation_subject = 'Gracias por contactarnos'
            confirmation_message = f'Hola {first_name},\n\nGracias por contactarnos. Hemos recibido tu mensaje y nos pondremos en contacto contigo a la brevedad.\n\nSaludos,\nEl equipo de MyProject'
            send_mail(confirmation_subject, confirmation_message, from_email, [email])

            # Redirecciona al template de saludo
            return redirect('saludo')
    else:
        form = ContactForm()

    return render(request, 'contact.html', {'form': form})

def saludo(request):
    return render(request, 'saludo.html')
