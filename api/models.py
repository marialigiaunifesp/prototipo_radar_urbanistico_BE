# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Documentos(models.Model):
    id_documento = models.BigAutoField(primary_key=True)
    documento = models.BinaryField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'documentos'


class Instituicao(models.Model):
    nome = models.TextField(blank=True, null=True)
    telefone1 = models.BigIntegerField(blank=True, null=True)
    telefone2 = models.BigIntegerField(blank=True, null=True)
    endereco = models.TextField(blank=True, null=True)
    cidade = models.TextField(blank=True, null=True)
    estado = models.TextField(blank=True, null=True)
    tipo_instituicao = models.TextField(blank=True, null=True)
    logo = models.ForeignKey(Documentos, models.SET_NULL, db_column='logo', blank=True, null=True)
    data_cadastro = models.DateField(blank=True, null=True)
    id_instituicao = models.BigAutoField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'instituicao'


class Usuario(models.Model):
    login = models.TextField(blank=True, null=True)
    senha_criptografa = models.TextField(blank=True, null=True)
    data_cadastro_usuario = models.DateField(blank=True, null=True)
    usuario_ativo = models.BooleanField(blank=True, null=True)
    tipo_usuario = models.IntegerField(blank=True, null=True)
    nome_usuario = models.TextField(blank=True, null=True)
    cpf = models.BigIntegerField(blank=True, null=True)
    email = models.TextField(blank=True, null=True)
    telefone1 = models.BigIntegerField(blank=True, null=True)
    telefone2 = models.BigIntegerField(blank=True, null=True)
    foto = models.ForeignKey(Documentos, models.SET_NULL, db_column='foto', blank=True, null=True)
    id_instituicao = models.ForeignKey(Instituicao, models.SET_NULL, db_column='id_instituicao', blank=True, null=True)
    id_usuario = models.BigAutoField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'usuario'


class Cadastro(models.Model):
    id_cadastro = models.BigAutoField(primary_key=True)
    id_usuario_criador = models.ForeignKey(Usuario, models.SET_NULL, db_column='id_usuario_criador', blank=True, null=True)
    data_criacao = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cadastro'


class CadastroVersao(models.Model):
    nome = models.TextField(blank=True, null=True)
    processo_numero = models.IntegerField(blank=True, null=True)
    processo_parte_nome = models.IntegerField(blank=True, null=True)
    processo_parte_documento = models.ForeignKey(Documentos, models.SET_NULL, db_column='processo_parte_documento', blank=True, null=True)
    processo_advogado_nome = models.TextField(blank=True, null=True)
    processo_advogado_oab = models.TextField(blank=True, null=True)
    processo_carta_precatorio = models.TextField(blank=True, null=True)
    processo_documento_delegacia = models.ForeignKey(Documentos, models.SET_NULL, db_column='processo_documento_delegacia', related_name='cadastroversao_processo_documento_delegacia_set', blank=True, null=True)
    processo_cda = models.TextField(blank=True, null=True)
    processo_classe = models.TextField(blank=True, null=True)
    processo_area = models.TextField(blank=True, null=True)
    processo_assunto = models.TextField(blank=True, null=True)
    processo_foro = models.TextField(blank=True, null=True)
    processo_vara = models.TextField(blank=True, null=True)
    processo_juiz = models.TextField(blank=True, null=True)
    processo_confte = models.TextField(blank=True, null=True)
    processo_requerida = models.TextField(blank=True, null=True)
    processo_data_movimentacoes = models.TextField(blank=True, null=True)
    processo_despacho = models.TextField(blank=True, null=True)
    processo_codigo_consulta = models.TextField(blank=True, null=True)
    processo_prazo = models.TextField(blank=True, null=True)
    oficio_numero = models.TextField(blank=True, null=True)
    oficio_orgao = models.TextField(blank=True, null=True)
    oficio_descricao = models.TextField(blank=True, null=True)
    matricula_numero = models.TextField(blank=True, null=True)
    matricula_numero_antigo = models.TextField(blank=True, null=True)
    matricula_cri = models.TextField(blank=True, null=True)
    matricula_comarca = models.TextField(blank=True, null=True)
    matricula_inscricao_mobiliaria = models.TextField(blank=True, null=True)
    matricula_endereco = models.TextField(blank=True, null=True)
    matricula_bairro = models.TextField(blank=True, null=True)
    matricula_regiao = models.TextField(blank=True, null=True)
    cpf_proprietario = models.BigIntegerField(blank=True, null=True)
    matricula_incra = models.TextField(blank=True, null=True)
    matricula_denominacao = models.TextField(blank=True, null=True)
    matricula_sicar = models.TextField(blank=True, null=True)
    matricula_sicar_sp = models.TextField(blank=True, null=True)
    matricula_proprietario = models.TextField(blank=True, null=True)
    matricula_vendedor = models.TextField(blank=True, null=True)
    matricula_aquisicao = models.TextField(blank=True, null=True)
    matricula_data_transacao = models.DateField(blank=True, null=True)
    matricula_ccir = models.TextField(blank=True, null=True)
    area_imovel = models.IntegerField(blank=True, null=True)
    unidade = models.TextField(blank=True, null=True)
    cnpf = models.BigIntegerField(blank=True, null=True)
    empreendimento = models.TextField(blank=True, null=True)
    vistoria_eletrica = models.TextField(blank=True, null=True)
    vistoria_agua = models.TextField(blank=True, null=True)
    vistoria_esgoto = models.TextField(blank=True, null=True)
    vistoria_iluminacao = models.TextField(blank=True, null=True)
    vistoria_drenagem = models.TextField(blank=True, null=True)
    vistoria_acesso = models.TextField(blank=True, null=True)
    vistoria_edificacoes = models.TextField(blank=True, null=True)
    vistoria_edificacoes_quantidade = models.TextField(blank=True, null=True)
    vistoria_uso = models.TextField(blank=True, null=True)
    vistoria_ponto = models.TextField(blank=True, null=True)
    vistoria_demarcacao = models.TextField(blank=True, null=True)
    proc_admin_advogado = models.TextField(blank=True, null=True)
    proc_admin_responsavel = models.TextField(blank=True, null=True)
    proc_admin_ponto_focal = models.TextField(blank=True, null=True)
    proc_admin_notificacao = models.TextField(blank=True, null=True)
    proc_admin_notificacao_prazo = models.TextField(blank=True, null=True)
    proc_admin_data = models.DateField(blank=True, null=True)
    proc_admin_boletim = models.TextField(blank=True, null=True)
    proc_admin_recurso = models.TextField(blank=True, null=True)
    proc_admin_reurb = models.TextField(blank=True, null=True)
    contato_telefone = models.TextField(blank=True, null=True)
    contato_email = models.TextField(blank=True, null=True)
    planta_parcelamento = models.TextField(blank=True, null=True)
    ficha_cadastral = models.ForeignKey(Documentos, models.SET_NULL, db_column='ficha_cadastral', related_name='cadastroversao_ficha_cadastral_set', blank=True, null=True)
    planialimetrico = models.TextField(blank=True, null=True)
    zona_uso = models.TextField(blank=True, null=True)
    aia = models.TextField(blank=True, null=True)
    local_latitude = models.FloatField(blank=True, null=True)
    local_longitude = models.FloatField(blank=True, null=True)
    poligono = models.TextField(blank=True, null=True)                  # TODO:This field type is a guess.
    ibge_aglomerado = models.IntegerField(blank=True, null=True)
    ibge_area_risco = models.IntegerField(blank=True, null=True)
    ibge_municipio = models.IntegerField(blank=True, null=True)
    distancia_saude = models.IntegerField(blank=True, null=True)
    distancia_educacao = models.IntegerField(blank=True, null=True)
    residuos_solidos = models.IntegerField(blank=True, null=True)
    distancia_transporte = models.IntegerField(blank=True, null=True)
    id_cadastro = models.ForeignKey(Cadastro, models.SET_NULL, db_column='id_cadastro', blank=True, null=True)
    id_usuario_criador = models.ForeignKey(Usuario, models.SET_NULL, db_column='id_usuario_criador', blank=True, null=True)
    data_atualizacao = models.DateField(blank=True, null=True)
    status = models.TextField(blank=True, null=True)
    versao_atual = models.BooleanField(blank=True, null=True)
    id_cadastro_versao = models.BigAutoField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'cadastro_versao'