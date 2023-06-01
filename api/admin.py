from django.contrib import admin
from .models import Documentos, Instituicao, Usuario, Cadastro, CadastroVersao

# Register your models here.

admin.site.register(Documentos)
admin.site.register(Instituicao)
admin.site.register(Usuario)
admin.site.register(Cadastro)
admin.site.register(CadastroVersao)
