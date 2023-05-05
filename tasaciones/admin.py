from django.contrib import admin
from django.contrib import messages
from .models import Tasacion

@admin.register(Tasacion)
class TasacionAdmin(admin.ModelAdmin):
    list_display = ['nombre_titular', 'cuit', 'direccion', 'telefono_contacto', 'impuesto_inmobiliario', 'email', 'fecha_creacion']
    search_fields = ['nombre_titular', 'cuit']
    list_filter = ['fecha_creacion']

    # Sobrescribe el método save_model para mostrar un mensaje cuando se agregue una nueva tasación.
    def save_model(self, request, obj, form, change):
        super().save_model(request, obj, form, change)
        if not change:  # Si no es una actualización, entonces es una nueva tasación.
            self.message_user(request, 'Hay una nueva solicitud de tasación. Por favor, revise la lista de tasaciones.', messages.SUCCESS)
