from rest_framework import serializers
from .models import *

'''
class Form:
	def __init__(self, variavel, valor, dataDocumento, referencia, documento, areaAnalise = None, coordinates = None):
		self.variavel = variavel
		self.valor = valor
		self.areaAnalise = areaAnalise
		self.dataDocumento = dataDocumento
		self.referencia = referencia
		self.documento = documento
		self.coordinates = coordinates

class Map:
	def __init__(self, coordinates):
		self.coordinates = coordinates
'''

class MatriculaSerializer(serializers.ModelSerializer):
	class Meta:
		model = MatriculaImovel
		fields = '__all__'

	def validate(self, data):
		if not data:
			raise serializers.ValidationError("Must include at least one field")
		return data

class ContratoSerializer(serializers.ModelSerializer):
	class Meta:
		model = ContratoCompraVenda
		fields = '__all__'

	def validate(self, data):
		if not data:
			raise serializers.ValidationError("Must include at least one field")
		return data


class OficioSerializer(serializers.ModelSerializer):
	class Meta:
		model = Oficio
		fields = '__all__'

	def validate(self, data):
		if not data:
			raise serializers.ValidationError("Must include at least one field")
		return data


class FormSerializer(serializers.Serializer):
	dataDocumento = serializers.CharField()
	referencia = serializers.CharField()
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