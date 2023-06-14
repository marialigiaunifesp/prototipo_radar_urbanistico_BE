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
class FormSerializer(serializers.Serializer):
	dataDocumento = serializers.CharField()
	referencia = serializers.CharField()

	def save(self):
		cv = CadastroVersao(
			data_atualizacao = self.validated_data['dataDocumento'],
			status = self.validated_data['referencia']
			)
		'''
		# Save to database
		cv.save()
		'''
		return cv
		


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