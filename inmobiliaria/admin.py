
from django.contrib import admin
from .models import Property, PropertyImage

class PropertyImageInline(admin.TabularInline):
    model = PropertyImage
    extra = 1
    max_num = 5

class PropertyAdmin(admin.ModelAdmin):
    list_display = ('title', 'property_type', 'price')
    inlines = [PropertyImageInline]

admin.site.register(Property, PropertyAdmin)