# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.contrib.gis.db import models


class AreaAnalise(models.Model):
    id_area = models.BigAutoField(primary_key=True)
    id_sicar = models.ForeignKey('Sicar', models.DO_NOTHING, db_column='id_sicar', blank=True, null=True)
    id_historico = models.ForeignKey('Historico', models.DO_NOTHING, db_column='id_historico', blank=True, null=True)
    nome = models.TextField(blank=True, null=True)
    nome_alternativo = models.TextField(blank=True, null=True)
    endereco = models.TextField(blank=True, null=True)
    referencia = models.TextField(blank=True, null=True)
    data_ultima_alteracao = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'area_analise'


class Arquivo(models.Model):
    id_arquivo = models.BigAutoField(primary_key=True)
    arquivo = models.BinaryField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'arquivo'


class BoletimOficial(models.Model):
    id_boletim_oficial = models.BigAutoField(primary_key=True)
    link_pub_edital = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'boletim_oficial'


class ConhecimentoLugar(models.Model):
    id_conhecimento_lugar = models.BigAutoField(primary_key=True)
    regiao = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'conhecimento_lugar'


class ContratoCompraVenda(models.Model):
    id_contrato_compra_venda = models.BigAutoField(primary_key=True)
    nome_empreendimento = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'contrato_compra_venda'


class Datageo(models.Model):
    id_datageo = models.BigAutoField(primary_key=True)
    distancia_saude_proximo = models.TextField(blank=True, null=True)
    distancia_educacao_proximo = models.TextField(blank=True, null=True)
    proximidade_local_atendido_transporte = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'datageo'


class DatageoAmbiente(models.Model):
    id_datageo_ambiente = models.BigIntegerField(primary_key=True)
    distancia_saude_proximo = models.TextField(blank=True, null=True)
    distancia_educacao_proximo = models.TextField(blank=True, null=True)
    proximidade_local_atendido_transporte = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'datageo_ambiente'


class DiversasFontes(models.Model):
    id_diversas_fontes = models.BigAutoField(primary_key=True)
    cpf_proprietario = models.TextField(blank=True, null=True)
    area_imovel = models.TextField(blank=True, null=True)
    ccir = models.TextField(blank=True, null=True)
    unidade = models.TextField(blank=True, null=True)
    cnpj = models.TextField(blank=True, null=True)
    telefone_contato = models.TextField(blank=True, null=True)
    email_contato = models.TextField(blank=True, null=True)
    possui_planta_parcelamento = models.TextField(blank=True, null=True)
    levantamento_planialtimetrico = models.TextField(blank=True, null=True)
    coordinada_aproximada = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'diversas_fontes'


class Documento(models.Model):
    id_documento = models.BigAutoField(primary_key=True)
    id_historico = models.ForeignKey('Historico', models.DO_NOTHING, db_column='id_historico', blank=True, null=True)
    id_area = models.ForeignKey(AreaAnalise, models.DO_NOTHING, db_column='id_area', blank=True, null=True)
    id_usuario_criador = models.ForeignKey('Usuario', models.DO_NOTHING, db_column='id_usuario_criador', blank=True, null=True)
    id_arquivo = models.ForeignKey(Arquivo, models.DO_NOTHING, db_column='id_arquivo', blank=True, null=True)
    id_processo_judicial = models.ForeignKey('ProcessoJudicial', models.DO_NOTHING, db_column='id_processo_judicial', blank=True, null=True)
    id_matricula_imovel = models.ForeignKey('MatriculaImovel', models.DO_NOTHING, db_column='id_matricula_imovel', blank=True, null=True)
    id_conhecimento_lugar = models.ForeignKey(ConhecimentoLugar, models.DO_NOTHING, db_column='id_conhecimento_lugar', blank=True, null=True)
    id_oficio = models.ForeignKey('Oficio', models.DO_NOTHING, db_column='id_oficio', blank=True, null=True)
    id_compra_venda = models.ForeignKey(ContratoCompraVenda, models.DO_NOTHING, db_column='id_compra_venda', blank=True, null=True)
    id_vistoria = models.ForeignKey('Vistoria', models.DO_NOTHING, db_column='id_vistoria', blank=True, null=True)
    id_processo_administrativo = models.ForeignKey('ProcessoAdministrativo', models.DO_NOTHING, db_column='id_processo_administrativo', blank=True, null=True)
    id_boletim_oficial = models.ForeignKey(BoletimOficial, models.DO_NOTHING, db_column='id_boletim_oficial', blank=True, null=True)
    id_ficha_socioeconomico = models.ForeignKey('FichaSocioeconomico', models.DO_NOTHING, db_column='id_ficha_socioeconomico', blank=True, null=True)
    id_legislacao = models.ForeignKey('Legislacao', models.DO_NOTHING, db_column='id_legislacao', blank=True, null=True)
    id_datageo_ambiente = models.ForeignKey(DatageoAmbiente, models.DO_NOTHING, db_column='id_datageo_ambiente', blank=True, null=True)
    id_ibge = models.ForeignKey('Ibge', models.DO_NOTHING, db_column='id_ibge', blank=True, null=True)
    id_datageo = models.ForeignKey(Datageo, models.DO_NOTHING, db_column='id_datageo', blank=True, null=True)
    id_diversas_fontes = models.ForeignKey(DiversasFontes, models.DO_NOTHING, db_column='id_diversas_fontes', blank=True, null=True)
    id_srid_projecao = models.ForeignKey('SpatialRefSys', models.DO_NOTHING, db_column='id_srid_projecao', blank=True, null=True)
    coordinates = models.PointField(srid=0, blank=True, null=True)
    data_atualizacao = models.DateField(blank=True, null=True)
    ultima_versao = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'documento'


class FichaSocioeconomico(models.Model):
    id_ficha_socioeconomico = models.BigAutoField(primary_key=True)
    ficha_cadastramento_individual = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ficha_socioeconomico'


class Historico(models.Model):
    id_historico = models.BigAutoField(primary_key=True)
    id_usuario_criador = models.ForeignKey('Usuario', models.DO_NOTHING, db_column='id_usuario_criador', blank=True, null=True)
    data_criacao = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'historico'


class Ibge(models.Model):
    id_ibge = models.BigAutoField(primary_key=True)
    aglomerado_subnormal = models.TextField(blank=True, null=True)
    area_risco = models.TextField(blank=True, null=True)
    cod_mun = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ibge'


class Instituicao(models.Model):
    id_instituicao = models.BigAutoField(primary_key=True)
    logo = models.ForeignKey(Arquivo, models.DO_NOTHING, db_column='logo', blank=True, null=True)
    nome = models.TextField(blank=True, null=True)
    data_cadastro = models.DateField(blank=True, null=True)
    telefone1 = models.BigIntegerField(blank=True, null=True)
    telefone2 = models.BigIntegerField(blank=True, null=True)
    endereco = models.TextField(blank=True, null=True)
    cidade = models.TextField(blank=True, null=True)
    estado = models.TextField(blank=True, null=True)
    tipo = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'instituicao'


class Legislacao(models.Model):
    id_legislacao = models.BigAutoField(primary_key=True)
    zona_uso = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'legislacao'


class MatriculaImovel(models.Model):
    id_matricula_imovel = models.BigAutoField(primary_key=True)
    numero = models.TextField(blank=True, null=True)
    numero_antigo = models.TextField(blank=True, null=True)
    cri = models.TextField(blank=True, null=True)
    comarca = models.TextField(blank=True, null=True)
    inscricao_imobiliaria = models.TextField(blank=True, null=True)
    endereco = models.TextField(blank=True, null=True)
    bairro = models.TextField(blank=True, null=True)
    regiao = models.TextField(blank=True, null=True)
    denominacao_imovel = models.TextField(blank=True, null=True)
    codigo_incra = models.TextField(blank=True, null=True)
    sicar = models.TextField(blank=True, null=True)
    sicar_sp = models.TextField(blank=True, null=True)
    proprietario = models.TextField(blank=True, null=True)
    vendedor = models.TextField(blank=True, null=True)
    forma_aquisicao = models.TextField(blank=True, null=True)
    data_transacao = models.TextField(blank=True, null=True)
    ccir = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'matricula_imovel'


class Oficio(models.Model):
    id_oficio = models.BigAutoField(primary_key=True)
    numero = models.BigIntegerField(blank=True, null=True)
    orgao = models.TextField(blank=True, null=True)
    comentario = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'oficio'


class Permissao(models.Model):
    id_permissao = models.BigAutoField(primary_key=True)
    tipo = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'permissao'


class Pessoa(models.Model):
    id_pessoa = models.BigAutoField(primary_key=True)
    id_area = models.ForeignKey(AreaAnalise, models.DO_NOTHING, db_column='id_area', blank=True, null=True)
    nome = models.TextField(blank=True, null=True)
    rg = models.BigIntegerField(blank=True, null=True)
    cpf = models.BigIntegerField(blank=True, null=True)
    tipo = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pessoa'


class ProcessoAdministrativo(models.Model):
    id_processo_administrativo = models.BigAutoField(primary_key=True)
    avogado_parte = models.TextField(blank=True, null=True)
    responsavel_tecnico_parte = models.TextField(blank=True, null=True)
    ponto_focal_moradores = models.TextField(blank=True, null=True)
    notificacao = models.TextField(blank=True, null=True)
    prazo_manifestacao = models.TextField(blank=True, null=True)
    data_publicacao_notificacao = models.TextField(blank=True, null=True)
    recurso_notificacao = models.TextField(blank=True, null=True)
    processo_reurb = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'processo_administrativo'


class ProcessoJudicial(models.Model):
    id_processo_judicial = models.BigAutoField(primary_key=True)
    numero_processo = models.TextField(blank=True, null=True)
    nome_parte_requerente = models.TextField(blank=True, null=True)
    nome_parte_requerida = models.TextField(blank=True, null=True)
    rg_requerida = models.TextField(blank=True, null=True)
    rg_requerente = models.TextField(blank=True, null=True)
    cpf_requetida = models.TextField(blank=True, null=True)
    cpf_requerente = models.TextField(blank=True, null=True)
    numero_carta = models.TextField(blank=True, null=True)
    nome_advogado = models.TextField(blank=True, null=True)
    oab = models.TextField(blank=True, null=True)
    documento_delegacia = models.TextField(blank=True, null=True)
    cda = models.TextField(blank=True, null=True)
    classe = models.TextField(blank=True, null=True)
    area = models.TextField(blank=True, null=True)
    assunto = models.TextField(blank=True, null=True)
    foro = models.TextField(blank=True, null=True)
    vara = models.TextField(blank=True, null=True)
    juiz = models.TextField(blank=True, null=True)
    confte = models.TextField(blank=True, null=True)
    data_movimentacoes = models.TextField(blank=True, null=True)
    despacho = models.TextField(blank=True, null=True)
    codigo_consulta_processo = models.TextField(blank=True, null=True)
    prazo_manifestacao_judicial = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'processo_judicial'


class SpatialRefSys(models.Model):
    srid = models.IntegerField(primary_key=True)
    auth_name = models.CharField(max_length=256, blank=True, null=True)
    auth_srid = models.IntegerField(blank=True, null=True)
    srtext = models.CharField(max_length=2048, blank=True, null=True)
    proj4text = models.CharField(max_length=2048, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'spatial_ref_sys'


class Sicar(models.Model):
    id_sicar = models.AutoField(primary_key=True)
    geom = models.MultiPolygonField(srid=4674, blank=True, null=True)
    cod_imovel = models.CharField(db_column='COD_IMOVEL', blank=True, null=True)  # Field name made lowercase.
    num_area = models.FloatField(db_column='NUM_AREA', blank=True, null=True)  # Field name made lowercase.
    cod_estado = models.CharField(db_column='COD_ESTADO', blank=True, null=True)  # Field name made lowercase.
    nom_munici = models.CharField(db_column='NOM_MUNICI', blank=True, null=True)  # Field name made lowercase.
    num_modulo = models.FloatField(db_column='NUM_MODULO', blank=True, null=True)  # Field name made lowercase.
    tipo_imove = models.CharField(db_column='TIPO_IMOVE', blank=True, null=True)  # Field name made lowercase.
    situacao = models.CharField(db_column='SITUACAO', blank=True, null=True)  # Field name made lowercase.
    condicao_i = models.CharField(db_column='CONDICAO_I', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'sicar'


class Usuario(models.Model):
    id_usuario = models.BigAutoField(primary_key=True)
    id_permissao = models.ForeignKey(Permissao, models.DO_NOTHING, db_column='id_permissao', blank=True, null=True)
    foto = models.ForeignKey(Arquivo, models.DO_NOTHING, db_column='foto', blank=True, null=True)
    id_instituicao = models.ForeignKey(Instituicao, models.DO_NOTHING, db_column='id_instituicao', blank=True, null=True)
    login = models.TextField(blank=True, null=True)
    senha_criptografa = models.TextField(blank=True, null=True)
    data_cadastro_usuario = models.DateField(blank=True, null=True)
    usuario_ativo = models.BooleanField(blank=True, null=True)
    nome_usuario = models.TextField(blank=True, null=True)
    cpf = models.BigIntegerField(blank=True, null=True)
    email = models.TextField(blank=True, null=True)
    telefone1 = models.BigIntegerField(blank=True, null=True)
    telefone2 = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'usuario'


class Vistoria(models.Model):
    id_vistoria = models.BigAutoField(primary_key=True)
    data = models.TextField(blank=True, null=True)
    energia_eletrica = models.TextField(blank=True, null=True)
    abastecimento_agua = models.TextField(blank=True, null=True)
    coleta_tratamento_esgoto = models.TextField(blank=True, null=True)
    iluminacao_publica = models.TextField(blank=True, null=True)
    drenagem_pluvial = models.TextField(blank=True, null=True)
    pavimentacao = models.TextField(blank=True, null=True)
    local_parcelada = models.TextField(blank=True, null=True)
    existencia_edificacoes = models.TextField(blank=True, null=True)
    quantidade_aproximada_edificacoes = models.TextField(blank=True, null=True)
    uso_constatado = models.TextField(blank=True, null=True)
    ponto_atencao = models.TextField(blank=True, null=True)
    lotes_demarcados = models.TextField(blank=True, null=True)
    coleta_residuos_solidos = models.TextField(blank=True, null=True)
    proximidade_local_transporte = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'vistoria'
