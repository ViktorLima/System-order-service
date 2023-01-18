from django.contrib import admin
from . models import Categoria, Cliente

class ClienteAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome', 'sobrenome', 'telefone', 'email',
                    'data', 'categoria')
    list_display_links = ('id', 'nome')
    list_per_page = 10
    search_fields = ('nome', 'telefone')


admin.site.register(Categoria)
admin.site.register(Cliente, ClienteAdmin)
