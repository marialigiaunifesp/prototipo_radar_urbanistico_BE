from django.views.decorators.csrf import csrf_exempt
from django.http import FileResponse
from rest_framework.decorators import api_view, parser_classes
from rest_framework.response import Response
from rest_framework.parsers import JSONParser, MultiPartParser
from rest_framework import status, generics
from .custom_serializers import FormSerializer, SicarSerializer, FileSerializer
from .serializers import *
import io
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
	str_json = serialize("geojson", obj, geometry_field="geom", srid = 4674)
	serializer = json.loads(str_json)
	
	return Response(serializer)

@api_view(['GET'])
@csrf_exempt
def getInfo(request, id_sicar):
	area = AreaAnalise.objects.get(id_sicar = id_sicar)
	docs = Documento.objects.filter(id_area = area.id_area).exclude(id_matricula_imovel = None)
	mi_set = [doc.id_matricula_imovel for doc in docs]
	mi_serializer = MatriculaSerializer(mi_set, many=True)
	clean_data = mi_serializer.to_representation(mi_serializer.data)
	form_data = FormSerializer(mi_serializer.data[0])
	teste = Doc()
	return Response(teste)
	# return Response(mi_serializer.data)


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
