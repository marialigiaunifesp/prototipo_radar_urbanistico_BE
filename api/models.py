# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AreaAnalise(models.Model):
    id_area = models.BigAutoField(primary_key=True)
    id_historico = models.ForeignKey('Historico', models.DO_NOTHING, db_column='id_historico', blank=True, null=True)
    srid_projecao = models.ForeignKey('SpatialRefSys', models.DO_NOTHING, db_column='srid_projecao', blank=True, null=True)
    nome = models.TextField(blank=True, null=True)
    nome_alternativo = models.TextField(blank=True, null=True)
    area = models.TextField(blank=True, null=True)  # This field type is a guess.
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


class Documento(models.Model):
    id_documento = models.BigAutoField(primary_key=True)
    id_oficio = models.ForeignKey('Oficio', models.DO_NOTHING, db_column='id_oficio', blank=True, null=True)
    coordinates = models.TextField(blank=True, null=True)  # This field type is a guess.
    data_atualizacao = models.DateField(blank=True, null=True)
    ultima_versao = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'documento'


class Historico(models.Model):
    id_historico = models.BigAutoField(primary_key=True)
    id_usuario_criador = models.ForeignKey('Usuario', models.DO_NOTHING, db_column='id_usuario_criador', blank=True, null=True)
    data_criacao = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'historico'


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


class SpatialRefSys(models.Model):
    srid = models.IntegerField(primary_key=True)
    auth_name = models.CharField(max_length=256, blank=True, null=True)
    auth_srid = models.IntegerField(blank=True, null=True)
    srtext = models.CharField(max_length=2048, blank=True, null=True)
    proj4text = models.CharField(max_length=2048, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'spatial_ref_sys'


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
