from .models import Logo

def logo_image(request):
    logo = Logo.objects.first()
    logo_url = logo.image.url if logo else ''
    return {'logo_url': logo_url}