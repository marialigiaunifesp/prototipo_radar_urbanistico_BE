from django.contrib import admin

from .models import AreaAnalise, Arquivo, Documento, Historico, Instituicao, Oficio, Permissao, Pessoa, Usuario

# Register your models here.

admin.site.register(AreaAnalise)
admin.site.register(Arquivo)
admin.site.register(Documento)
admin.site.register(Historico)
admin.site.register(Instituicao)
admin.site.register(Oficio)
admin.site.register(Permissao)
admin.site.register(Pessoa)
admin.site.register(Usuario)