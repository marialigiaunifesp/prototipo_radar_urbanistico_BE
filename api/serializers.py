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


class FormSerializer(serializers.Serializer):
	dataDocumento = serializers.CharField()
	referencia = serializers.CharField()
	oficio = OficioSerializer()
	contrato_compra_venda = ContratoSerializer()

	def save(self):
		oficio = self.validated_data['oficio']
		contrato = self.validated_data['contrato_compra_venda']

		doc = Documento(data_atualizacao = self.validated_data[	'dataDocumento'])
		history = AreaAnalise(referencia = self.validated_data['referencia'])
		
		# this creates 
		# oficio_instance = Oficio.objects.create(**oficio)
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