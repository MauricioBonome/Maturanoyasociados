from django.contrib import admin
from .models import Logo, SiteIcon


class LogoAdmin(admin.ModelAdmin):
    list_display = ('id', 'image',)
    list_display_links = ('id', 'image',)
admin.site.register(Logo, LogoAdmin)
admin.site.register(SiteIcon)