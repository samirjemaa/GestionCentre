from django.contrib import admin

# Register your models here.
from locaux.models import local


# admin.site.register(local)

class LocalAdmin(admin.ModelAdmin):
    fields = ('libelle', ('nb_post', 'nb_heure'), ('type', 'etat'))
    list_display = ('libelle', 'nb_post', 'nb_heure', 'type', 'etat', 'update_at')
    list_filter = ('etat', 'type', 'update_at')
    ordering = ('libelle',)
    search_fields = ('libelle', 'etat', 'type', 'update_at')


admin.site.register(local, LocalAdmin)
