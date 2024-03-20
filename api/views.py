from django.contrib.gis.geos import GEOSGeometry
from django.views.decorators.csrf import csrf_exempt
from django.http import FileResponse, HttpResponse
from rest_framework.decorators import api_view, parser_classes
from rest_framework.response import Response
from rest_framework.parsers import JSONParser, MultiPartParser
from rest_framework import status, generics
from .custom_serializers import FormSerializer, FileSerializer
from .serializers import *
import os, io
from .models import *
from django.core.serializers import serialize
import json
from django.shortcuts import get_object_or_404 	


@api_view(['POST'])
@csrf_exempt
def formCreate(request):
	serializer = FormSerializer(data = request.data)

	if(serializer.is_valid()):
		doc = serializer.save()
		return Response(doc.id_documento, status = status.HTTP_201_CREATED)

	else:
		print(serializer.errors)
		return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

#TODO: Remove later
@csrf_exempt
def postSicar(request):
	ct = 0
	with open('../prototipo_radar_urbanistico_FE/public/sicar_area_imovel.geojson') as fd:
		gj = json.load(fd)
		
		for feature in gj['features']:
			fprop = feature['properties']
			geom_str = '''{
						"crs": { "type": "name", "properties": { "name": "urn:ogc:def:crs:EPSG::3857" } },
						''' + str(feature['geometry'])[1:-1] + '}'
			
			sicar_obj = Sicar(
					cod_imovel = fprop['COD_IMOVEL'],
					num_area = fprop['NUM_AREA'],
					cod_estado = fprop['COD_ESTADO'],
					nom_munici = fprop['NOM_MUNICI'],
					num_modulo = fprop['NUM_MODULO'],
					tipo_imove = fprop['TIPO_IMOVE'],
					situacao = fprop['SITUACAO'],
					condicao_i = fprop['CONDICAO_I'],
					geom = GEOSGeometry(geom_str)
				)

			if sicar_obj:
				sicar_obj.save()
				area = AreaAnalise(id_sicar = sicar_obj)
				area.save()

		return(HttpResponse('Ok'))
	return(HttpResponse('Some error'))

@api_view(['POST'])
@csrf_exempt
def formPostFile(request):
	serializer = FileSerializer(data = request.data)
	if(serializer.is_valid()):
		id_documento = request.data.get('id_documento')
		obj = serializer.save(id_documento)
		return Response(serializer.data, status = status.HTTP_201_CREATED)

	else:
		print(serializer.errors)
		return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
@csrf_exempt
def getSicar(request):
	obj = Sicar.objects.all()
	str_json = serialize("geojson", obj, geometry_field="geom", srid = 3857)
	serializer = json.loads(str_json)
	
	return Response(serializer)

@api_view(['POST'])
@csrf_exempt
def token(request):
	try:
		user_obj = Usuario.objects.get(login = request.data['username'], senha_criptografa = request.data['password'])

	except Usuario.DoesNotExist:
		return Response (status = 205)

	except Usuario.MultipleObjectsReturned:
		return Response(status = 205)

	else:
		serializer = UsuarioSerializer(user_obj)
		if serializer.is_valid:
			return Response(serializer.data, status.HTTP_200_OK)
		else:
			return Response(status = status.HTTP_500_INTERNAL_SERVER_ERROR)

		

def download_arquivo(request, id_arquivo):
	arquivo = get_object_or_404(Arquivo, id_arquivo=id_arquivo)
	response = FileResponse(arquivo.arquivo)
	response['Content-Disposition'] = f'attachment; filename="{arquivo}"'
	with open('file.ext', 'wb') as f:
		f.write(arquivo.arquivo)
	
	return response

class DocumentoView(generics.ListAPIView):
	serializer_class = DocumentoSerializer
	lookup_url_kwarg = 'id_sicar'

	def get_queryset(self):
		id_sicar = self.kwargs.get(self.lookup_url_kwarg)
		area = AreaAnalise.objects.get(id_sicar = id_sicar)
		
		documento = Documento.objects.filter(id_area = area.id_area)
		return documento
