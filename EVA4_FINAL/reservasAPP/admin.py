from django.contrib import admin
from .models import Reserva

# Register your models here.
class ReservaAdmin(admin.ModelAdmin):
    list_display = ('id','nombre','telefono','fecha_reserva','hora','cantidad_personas','estado','observacion')
    list_filter = ('estado', 'fecha_reserva')

    fieldsets = (
        (None, {'fields':('nombre','telefono','fecha_reserva','hora','cantidad_personas','estado','observacion')}),
    )

admin.site.register(Reserva, ReservaAdmin)