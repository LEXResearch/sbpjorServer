from django.contrib import admin
from .models import Trabalho, Mesa, Atividade, Cronograma, CategoriaAtividade, Dia, Evento


admin.site.register(Trabalho)
admin.site.register(Mesa)
admin.site.register(Atividade)
admin.site.register(Cronograma)
admin.site.register(CategoriaAtividade)
admin.site.register(Dia)
admin.site.register(Evento)
