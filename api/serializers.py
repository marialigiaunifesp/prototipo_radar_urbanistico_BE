from rest_framework import serializers
from .models import *
from django.core.serializers import serialize
from geojson_serializer.serializers import geojson_serializer

'''
# MODEL-BASED SERIALIZERS
'''

# Boletim oficial
class BoletimOficialSerializer(serializers.ModelSerializer):
	class Meta:
		model = BoletimOficial
		fields = '__all__'

	def validate(self, data):
		if not data:
			raise serializers.ValidationError("Must include at least one field")
		return data

# Conhecimento do lugar
class ConhecimentoLugarSerializer(serializers.ModelSerializer):
	class Meta:
		model = ConhecimentoLugar
		fields = '__all__'

	def validate(self, data):
		if not data:
			raise serializers.ValidationError("Must include at least one field")
		return data

# Contrato compra venda 
class ContratoSerializer(serializers.ModelSerializer):
	class Meta:
		model = ContratoCompraVenda
		fields = '__all__'

	def validate(self, data):
		if not data:
			raise serializers.ValidationError("Must include at least one field")
		return data

# Dados geograficos
class DatageoSerializer(serializers.ModelSerializer):
	class Meta:
		model = Datageo
		fields = '__all__'

	def validate(self, data):
		if not data:
			raise serializers.ValidationError("Must include at least one field")
		return data

# Datageo ambiente
class DatageoAmbienteSerializer(serializers.ModelSerializer):
	class Meta:
		model = DatageoAmbiente
		fields = '__all__'

	def validate(self, data):
		if not data:
			raise serializers.ValidationError("Must include at least one field")
		return data

# Diversas Fontes
class DiversasFontesSerializer(serializers.ModelSerializer):
	class Meta:
		model = DiversasFontes
		fields = '__all__'

	def validate(self, data):
		if not data:
			raise serializers.ValidationError("Must include at least one field")
		return data

# Ficha de cadastramento socioeconomico
class FichaSocioeconomicoSerializer(serializers.ModelSerializer):
	class Meta:
		model = FichaSocioeconomico
		fields = '__all__'

	def validate(self, data):
		if not data:
			raise serializers.ValidationError("Must include at least one field")
		return data
# IBGE
class IbgeSerializer(serializers.ModelSerializer):
	class Meta:
		model = Ibge
		fields = '__all__'

	def validate(self, data):
		if not data:
			raise serializers.ValidationError("Must include at least one field")
		return data	

# Legislacao
class LegislacaoSerializer(serializers.ModelSerializer):
	class Meta:
		model = Legislacao
		fields = '__all__'

	def validate(self, data):
		if not data:
			raise serializers.ValidationError("Must include at least one field")
		return data

# Matricula do imovel
class MatriculaSerializer(serializers.ModelSerializer):
	class Meta:
		model = MatriculaImovel
		fields = '__all__'

	def validate(self, data):
		if not data:
			raise serializers.ValidationError("Must include at least one field")
		return data

	def to_representation(self, instance):
		data = super().to_representation(instance)
		return {key: value for key, value in data.items() if value is not None}

# Oficio
class OficioSerializer(serializers.ModelSerializer):
	class Meta:
		model = Oficio
		fields = '__all__'

	def validate(self, data):
		if not data:
			raise serializers.ValidationError("Must include at least one field")
		return data

#Processo Administrativo
class ProcessoAdministrativoSerializer(serializers.ModelSerializer):
	class Meta:
		model = ProcessoAdministrativo
		fields = '__all__'

	def validate(self, data):
		if not data:
			raise serializers.ValidationError("Must include at least one field")
		return data

# Processo Judicial
class ProcessoJudicialSerializer(serializers.ModelSerializer):
	class Meta:
		model = ProcessoJudicial
		fields = '__all__'

	def validate(self, data):
		if not data:
			raise serializers.ValidationError("Must include at least one field")
		return data

# Vistoria
class VistoriaSerializer(serializers.ModelSerializer):
	class Meta:
		model = Vistoria
		fields = '__all__'

	def validate(self, data):
		if not data:
			raise serializers.ValidationError("Must include at least one field")
		return data

class DocumentoSerializer(serializers.ModelSerializer):
	id_boletim_oficial = BoletimOficialSerializer(required=False, allow_null=True)
	id_conhecimento_lugar = ConhecimentoLugarSerializer(required=False, allow_null=True)
	id_contrato_compra_venda = ContratoSerializer(required=False, allow_null=True)
	id_datageo = DatageoSerializer(required=False, allow_null=True)
	id_datageo_ambiente = DatageoAmbienteSerializer(required=False, allow_null=True)
	id_diversas_fontes = DiversasFontesSerializer(required=False, allow_null=True)
	id_ficha_socioeconomico = FichaSocioeconomicoSerializer(required=False, allow_null=True)
	id_ibge = IbgeSerializer(required=False, allow_null=True)
	id_legislacao = LegislacaoSerializer(required=False, allow_null=True)
	id_matricula_imovel = MatriculaSerializer(required=False, allow_null=True)
	id_oficio = OficioSerializer(required=False, allow_null=True)
	id_processo_administrativo = ProcessoJudicialSerializer(required=False, allow_null=True)
	id_processo_judicial = ProcessoJudicialSerializer(required=False, allow_null=True)
	id_vistoria = VistoriaSerializer(required=False, allow_null=True)

	class Meta:
		model = Documento
		fields = [
		'id_boletim_oficial',
		'id_conhecimento_lugar',
		'id_contrato_compra_venda',
		'id_datageo',
		'id_datageo_ambiente',
		'id_diversas_fontes',
		'id_ficha_socioeconomico',
		'id_ibge',
		'id_legislacao',
		'id_matricula_imovel',
		'id_oficio',
		'id_processo_administrativo',
		'id_processo_judicial',
		'id_vistoria',
		]
	"""
	def get_id_matricula_imovel(self, instance):
		id_matricula_imovel = instance.id_matricula_imovel.objects.all()
		if id_matricula_imovel.exists():
			return MatriculaSerializer(id_matricula_imovel, many = True).data
		else:
			return None
	"""
class UsuarioSerializer(serializers.ModelSerializer):
	token = serializers.ReadOnlyField()

	class Meta:
		model = Usuario
		fields = ['login', 'token']

@geojson_serializer('geom')
class SicarSerializer(serializers.ModelSerializer):
	class Meta:
		model = Sicar
		fields = '__all__'
