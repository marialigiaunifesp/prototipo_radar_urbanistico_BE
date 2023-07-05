from rest_framework import serializers
from .models import *
from django.core.serializers import serialize
from .serializers import *
from geojson_serializer.serializers import geojson_serializer

'''
# CUSTOM SERIALIZERS
'''

class FormSerializer(serializers.Serializer):
	# Native datypes
	dataDocumento = serializers.CharField(required = False)
	referencia = serializers.CharField(required = False)
	id_sicar = serializers.IntegerField()

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

	def save(self):
		id_sicar_obj = self.validated_data['id_sicar']
		if(AreaAnalise.objects.filter(id_sicar = id_sicar_obj).exists()):
			area = AreaAnalise.objects.get(id_sicar = id_sicar_obj)
		else:
			area = AreaAnalise()
			area.id_sicar = Sicar(id_sicar_obj)
			area.save()


		doc = Documento()
		doc.id_area = area
		# history = AreaAnalise(referencia = self.validated_data['referencia'])
		
		if('boletim_oficial' in self.validated_data):
			boletim_oficial_obj = self.validated_data['boletim_oficial']
			boletim_oficial_instance = BoletimOficial.objects.create(**boletim_oficial_obj)
			doc.id_boletim_oficial = boletim_oficial_instance


		if('conhecimento_lugar' in self.validated_data):
			conhecimento_lugar_obj = self.validated_data['conhecimento_lugar']
			conhecimento_lugar_instance = ConhecimentoLugar.objects.create(**conhecimento_lugar_obj)
			doc.id_conhecimento_lugar = conhecimento_lugar_instance
		
		if('contrato_compra_venda' in self.validated_data):
			contrato_obj = self.validated_data['contrato_compra_venda']
			contrato_instance = ContratoCompraVenda.objects.create(**contrato_obj)
			doc.id_compra_venda = contrato_instance

		
		if('datageo' in self.validated_data):
			datageo_obj = self.validated_data['datageo']
			datageo_instance = Datageo.objects.create(**datageo_obj)
			doc.id_datageo = datageo_instance

		if('datageo_ambiente' in self.validated_data):
			datageo_ambiente_obj = self.validated_data['datageo_ambiente']
			datageo_ambiente_instance = DatageoAmbiente.objects.create(**datageo_ambiente_obj)
			doc.id_datageo_ambiente = datageo_ambiente_instance

		if('diversas_fontes' in self.validated_data):
			diversas_fontes_obj = self.validated_data['diversas_fontes']
			diversas_fontes_instance = DiversasFontes.objects.create(**diversas_fontes_obj)
			doc.id_diversas_fontes = diversas_fontes_instance

		if('ficha_socioeconomico' in self.validated_data):
			ficha_socioeconomico_obj = self.validated_data['ficha_socioeconomico']
			ficha_socioeconomico_instance = FichaSocioeconomico.objects.create(**ficha_socioeconomico_obj)
			doc.id_ficha_socioeconomico = ficha_socioeconomico_instance

		if('IBGE' in self.validated_data):
			IBGE_obj = self.validated_data['IBGE']
			IBGE_instance = Ibge.objects.create(**IBGE_obj)
			doc.id_ibge = IBGE_instance

		if('legislacao' in self.validated_data):
			legislacao_obj = self.validated_data['legislacao']
			legislacao_instance = Legislacao.objects.create(**legislacao_obj)
			doc.id_legislacao = legislacao_instance

		if('processo_administrativo' in self.validated_data):
			processo_administrativo_obj = self.validated_data['processo_administrativo']
			processo_administrativo_instance = ProcessoAdministrativo.objects.create(**processo_administrativo_obj)
			doc.id_processo_administrativo = processo_administrativo_instance


		if('matricula_imovel' in self.validated_data):
			matricula_obj = self.validated_data['matricula_imovel']
			matricula_instance = MatriculaImovel.objects.create(**matricula_obj)
			doc.id_matricula_imovel = matricula_instance

		if('oficio' in self.validated_data):
			oficio_obj = self.validated_data['oficio']
			oficio_instance = Oficio.objects.create(**oficio_obj)
			doc.id_oficio = oficio_instance

		if('processo_judicial' in self.validated_data):
			processo_judicial_obj = self.validated_data['processo_judicial']
			processo_judicial_instance = ProcessoJudicial.objects.create(**processo_judicial_obj)
			doc.id_processo_judicial = processo_judicial_instance

		if('vistoria' in self.validated_data):
			vistoria_obj = self.validated_data['vistoria']
			vistoria_instance = Vistoria.objects.create(**vistoria_obj)
			doc.id_vistoria = vistoria_instance

		# Save to database
		doc.save()
		# history.save()
		# return sicar

class FileSerializer(serializers.Serializer):
	arquivo = serializers.FileField()

	def save(self):
		arquivo = self.validated_data.get("arquivo")
		file = Arquivo(arquivo = arquivo.read())
		file.save()
		return file