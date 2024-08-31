from django.contrib import admin
from .models import Cliente, Asesoramiento, Cita

# admin.site.register(Cliente)
# admin.site.register(Servicio)
# admin.site.register(Pedido)


@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = ("dni", "apellido", "nombre", "telefono")
    search_fields = ("dni", "apellido", "nombre", "telefono")
    ordering = ("apellido", "nombre")


@admin.register(Asesoramiento)
class AsesoramientoAdmin(admin.ModelAdmin):
    list_display = ("derecho", "descripcion", "disponible")
    list_filter = ("disponible",)
    search_fields = ("derecho",)
    ordering = ("derecho",)


@admin.register(Cita)
class CitaAdmin(admin.ModelAdmin):
    list_display = ("cliente", "derecho", "estado", "fecha_solicitud", "fecha_cita", "hora")
    list_filter = ("estado", "fecha_solicitud")
    search_fields = ("cliente__nombre", "asesoramiento__derecho")
    ordering = ("fecha_cita",)
    date_hierarchy = "fecha_solicitud"
