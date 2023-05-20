
from django.contrib import admin
from .models import Property, PropertyImage
from .models import Venta


class PropertyImageInline(admin.TabularInline):
    model = PropertyImage
    extra = 1
    max_num = 5

class PropertyAdmin(admin.ModelAdmin):
    list_display = ('title', 'property_type', 'price', 'vendido', 'alquilado')
    inlines = [PropertyImageInline]







class VentaAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'email', 'telefono', 'localidad', 'provincia', 'fecha')
    list_filter = ('provincia', 'fecha')
    search_fields = ('nombre', 'email', 'telefono')
    readonly_fields = ('fecha',)

admin.site.register(Venta, VentaAdmin)



admin.site.register(Property, PropertyAdmin)