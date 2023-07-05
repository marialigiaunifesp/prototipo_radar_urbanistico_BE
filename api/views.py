from django.views.decorators.csrf import csrf_exempt
from django.http import FileResponse
from rest_framework.decorators import api_view, parser_classes
from rest_framework.response import Response
from rest_framework.parsers import JSONParser, MultiPartParser
from rest_framework import status
from .custom_serializers import FormSerializer, SicarSerializer, FileSerializer
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
		obj = serializer.save()
		return Response(serializer.data, status = status.HTTP_201_CREATED)
	
	else:
		return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
@csrf_exempt
def formFile(request):
	serializer = FileSerializer(data = request.data)
	if 'arquivo' in request.FILES:
		print(request.FILES['arquivo'])

	if(serializer.is_valid()):
		obj = serializer.save()
		return Response(serializer.data, status = status.HTTP_201_CREATED)
	else:
		print(serializer.errors)
		return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)


def download_arquivo(request, id_arquivo):
    arquivo = get_object_or_404(Arquivo, id_arquivo=id_arquivo)
    response = FileResponse(arquivo.arquivo)
    response['Content-Disposition'] = f'attachment; filename="{arquivo}"'
    with open('file.ext', 'wb') as f:
    	f.write(arquivo.arquivo)
    return response


@api_view(['GET'])
@csrf_exempt
def getSicar(request):
	obj = Sicar.objects.all()
	str_json = serialize("geojson", obj, geometry_field="geom", srid = 4674)
	serializer = json.loads(str_json)
	
	return Response(serializer)
