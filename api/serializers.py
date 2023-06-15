from rest_framework import serializers
from .models import *

'''
# MODEL-BASED SERIALIZERS
'''

# Boletim oficial
class BoletimOficialSerializer(serializers.ModelSerializer):
	class Meta:
		model = BoletimOficial
		fields = '__all__'

# Conhecimento do lugar
class ConhecimentoLugarSerializer(serializers.ModelSerializer):
	class Meta:
		model = ConhecimentoLugar
		fields = '__all__'

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

# Datageo ambiente
class DatageoAmbienteSerializer(serializers.ModelSerializer):
	class Meta:
		model = DatageoAmbiente
		fields = '__all__'

# Diversas Fontes
class DiversasFontesSerializer(serializers.ModelSerializer):
	class Meta:
		model = DiversasFontes
		fields = '__all__'

# Ficha de cadastramento socioeconomico
class FichaSocioeconomicoSerializer(serializers.ModelSerializer):
	class Meta:
		model = FichaSocioeconomico
		fields = '__all__'

# IBGE
class IbgeSerializer(serializers.ModelSerializer):
	class Meta:
		model = Ibge
		fields = '__all__'

# Legislacao
class LegislacaoSerializer(serializers.ModelSerializer):
	class Meta:
		model = Legislacao
		fields = '__all__'

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

# Processo Judicial
class ProcessoJudicialSerializer(serializers.ModelSerializer):
	class Meta:
		model = ProcessoJudicial
		fields = '__all__'

# Vistoria
class VistoriaSerializer(serializers.ModelSerializer):
	class Meta:
		model = Vistoria
		fields = '__all__'


'''
# CUSTOM SERIALIZERS
'''
class FormSerializer(serializers.Serializer):
	# Native datypes
	dataDocumento = serializers.CharField()
	referencia = serializers.CharField()

	# Nested
	oficio = OficioSerializer(required = False)
	contrato_compra_venda = ContratoSerializer(required = False)
	matricula_imovel = MatriculaSerializer(required = False)

	def save(self):

		doc = Documento(data_atualizacao = self.validated_data[	'dataDocumento'])
		history = AreaAnalise(referencia = self.validated_data['referencia'])
		
		if('oficio' in self.validated_data):
			oficio_obj = self.validated_data['oficio']
			# creates instance 
			# oficio_instance = Oficio.objects.create(**oficio)
		
		if('contrato_compra_venda' in self.validated_data):
			contrato_obj = self.validated_data['contrato_compra_venda']
			# creates instance
			# contrato_instance = ContratoCompraVenda.objects.create(**contrato)

		if('matricula_imovel' in self.validated_data):
			matricula_obj = self.validated_data['matricula_imovel']
			# creates instance
			# contrato_instance = ContratoCompraVenda.objects.create(**contrato)

		'''
		# Save to database
		doc.save()
		history.save()
		'''
		return doc
		


	# documento = serializers.CharField()
	# coordinates = serializers.ListField(child = serializers.FloatField())


'''
class MapSerializer(serializers.Serializer):
	coordinates = serializers.ListField(
		child = serializers.FloatField()
	)

	def create(self, validated_data):
		return Map(**validated_data)
'''