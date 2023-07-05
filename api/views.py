from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view, parser_classes
from rest_framework.response import Response
from rest_framework.parsers import JSONParser, MultiPartParser
from rest_framework import status
from .serializers import FormSerializer, SicarSerializer, FileSerializer
import io
from .models import *
from django.core.serializers import serialize
import json

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
		print('its')
	if(serializer.is_valid()):
		obj = serializer.save()
		return Response(serializer.data, status = status.HTTP_201_CREATED)
	
	else:
		return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
@csrf_exempt
def getSicar(request):
	obj = Sicar.objects.all()
	str_json = serialize("geojson", obj, geometry_field="geom", srid = 4674)
	serializer = json.loads(str_json)
	
	return Response(serializer)
