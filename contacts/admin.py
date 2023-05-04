from django.contrib import admin
from .models import Contact

class ContactAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email', 'inquiry_type', 'created_at')
    search_fields = ('first_name', 'last_name', 'email', 'inquiry_type')
    list_filter = ('inquiry_type', 'created_at')

admin.site.register(Contact, ContactAdmin)