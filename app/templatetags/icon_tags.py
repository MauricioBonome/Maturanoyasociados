# myapp/templatetags/icon_tags.py

from django import template

from app.models import SiteIcon

register = template.Library()

@register.simple_tag
def get_site_icon():
    icon = SiteIcon.objects.first()  # Obtiene el primer objeto SiteIcon
    return icon.favicon.url if icon else None
