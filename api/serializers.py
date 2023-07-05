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

@geojson_serializer('geom')
class SicarSerializer(serializers.ModelSerializer):
	class Meta:
		model = Sicar
		fields = '__all__'
