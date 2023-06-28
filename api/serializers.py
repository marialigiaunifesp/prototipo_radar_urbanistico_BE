from rest_framework import serializers
from .models import *
from django.contrib.gis.geos import Point
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

@geojson_serializer('geom', 'crs')
class SicarSerializer(serializers.ModelSerializer):
	class Meta:
		model = Sicar
		fields = '__all__'

'''
# CUSTOM SERIALIZERS
'''


class FormSerializer(serializers.Serializer):
	# Native datypes
	dataDocumento = serializers.CharField()
	referencia = serializers.CharField()
	sicar = serializers.CharField()

	# Nested datatypes
	boletim_oficial = BoletimOficialSerializer(required = False)
	conhecimento_lugar = ConhecimentoLugarSerializer(required = False)
	contrato_compra_venda = ContratoSerializer(required = False)
	datageo = DatageoSerializer(required = False)
	datageo_ambiente = DatageoAmbienteSerializer(required = False)
	diversas_fontes = DiversasFontesSerializer(required = False)
	ficha_socioeconomico = FichaSocioeconomicoSerializer(required = False)
	IBGE = IbgeSerializer(required = False)
	legislacao = LegislacaoSerializer(required = False)
	matricula_imovel = MatriculaSerializer(required = False)
	oficio = OficioSerializer(required = False)
	processo_administrativo = ProcessoAdministrativoSerializer(required = False)
	processo_judicial = ProcessoJudicialSerializer(required = False)
	vistoria = VistoriaSerializer(required = False)
	sicar = SicarSerializer(required = False)

	def save(self):

		doc = Documento(data_atualizacao = self.validated_data[	'dataDocumento'])
		history = AreaAnalise(referencia = self.validated_data['referencia'])
		
		if('boletim_oficial' in self.validated_data):
			boletim_oficial_obj = self.validated_data['boletim_oficial']
			boletim_oficial_instance = BoletimOficial.objects.create(**boletim_oficial_obj)


		if('conhecimento_lugar' in self.validated_data):
			conhecimento_lugar_obj = self.validated_data['conhecimento_lugar']
			conhecimento_lugar_instance = ConhecimentoLugar.objects.create(**conhecimento_lugar_obj)
		
		if('contrato_compra_venda' in self.validated_data):
			contrato_obj = self.validated_data['contrato_compra_venda']
			contrato_instance = ContratoCompraVenda.objects.create(**contrato_obj)
		
		if('datageo' in self.validated_data):
			datageo_obj = self.validated_data['datageo']
			datageo_instance = Datageo.objects.create(**datageo_obj)

		if('datageo_ambiente' in self.validated_data):
			datageo_ambiente_obj = self.validated_data['datageo_ambiente']
			datageo_ambiente_instance = DatageoAmbiente.objects.create(**datageo_ambiente_obj)

		if('diversas_fontes' in self.validated_data):
			diversas_fontes_obj = self.validated_data['diversas_fontes']
			diversas_fontes_instance = DiversasFontes.objects.create(**diversas_fontes_obj)

		if('ficha_socioeconomico' in self.validated_data):
			ficha_socioeconomico_obj = self.validated_data['ficha_socioeconomico']
			ficha_socioeconomico_instance = FichaSocioeconomico.objects.create(**ficha_socioeconomico_obj)

		if('IBGE' in self.validated_data):
			IBGE_obj = self.validated_data['IBGE']
			IBGE_instance = Ibge.objects.create(**IBGE_obj)

		if('legislacao' in self.validated_data):
			legislacao_obj = self.validated_data['legislacao']
			legislacao_instance = Legislacao.objects.create(**legislacao_obj)

		if('processo_administrativo' in self.validated_data):
			processo_administrativo_obj = self.validated_data['processo_administrativo']
			processo_administrativo_instance = ProcessoAdministrativo.objects.create(**processo_administrativo_obj)


		if('matricula_imovel' in self.validated_data):
			matricula_obj = self.validated_data['matricula_imovel']
			matricula_instance = MatriculaImovel.objects.create(**matricula_obj)

		if('oficio' in self.validated_data):
			oficio_obj = self.validated_data['oficio']
			oficio_instance = Oficio.objects.create(**oficio_obj)

		if('processo_judicial' in self.validated_data):
			processo_judicial_obj = self.validated_data['processo_judicial']
			processo_judicial_instance = ProcessoJudicial.objects.create(**processo_judicial_obj)

		if('vistoria' in self.validated_data):
			vistoria_obj = self.validated_data['vistoria']
			vistoria_instance = Vistoria.objects.create(**vistoria_obj)

		if('sicar' in self.validated_data):
			sicar_obj = self.validated_data['sicar']
			sicar_instance = Sicar.objects.create(**sicar_obj)

		
		# Save to database
		# doc.save()
		# history.save()
		return doc

class GeometrySerializer(serializers.Serializer):
	coordinates = serializers.ListField(
		child = serializers.FloatField()
	)

class FeatureSerializer(serializers.Serializer):
	geometry = GeometrySerializer()

class CoordinateSerializer(serializers.Serializer):
	features = FeatureSerializer(many = True)

	def save(self):

		if('features' in self.validated_data):
			if('geometry' in self.validated_data['features'][0]):
				if('coordinates' in self.validated_data['features'][0]['geometry']):
					coord_obj = self.validated_data['features'][0]['geometry']['coordinates']
					coord_instance = Documento(coordinates = Point(coord_obj[0], coord_obj[1]))
					coord_instance.save()
		
		return coord_instance