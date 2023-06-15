from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view, parser_classes
from rest_framework.response import Response
from rest_framework.parsers import JSONParser, MultiPartParser
from rest_framework import status
from .serializers import FormSerializer
import io
from .models import *

@api_view(['POST'])
@csrf_exempt
def formCreate(request):
	# print(request.data)
	serializer = FormSerializer(data = request.data)
	if(serializer.is_valid()):
		obj = serializer.save()
		return Response(serializer.data, status = status.HTTP_201_CREATED)
	
	else:
		return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)



'''
@api_view(['POST'])
@csrf_exempt
def formCreate(request):
'''	
	#fjson = JSONParser().parse(request)
	#print(fjson)
'''
	serializer = FormSerializer(data = fjson)

	if(serializer.is_valid()):
		#TODO : define save
		serializer.save()
		return Response(serializer.data, status = status.HTTP_201_CREATED)
	
	return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
'''
	#return Response(status = status.HTTP_400_BAD_REQUEST)
'''
@api_view(['POST'])
@csrf_exempt
def mapCreate(request):
	fjson = JSONParser().parse(request)
	serializer = MapSerializer(data = fjson)

	if(serializer.is_valid()):
		#TODO : define save
		serializer.save()
		return Response(serializer.data, status = status.HTTP_201_CREATED)

	return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
'''
'''	data = JSONParser().parse(request)
	serializer = FormSerializer(data=data)
	
	if serializer.is_valid():
		print('Valid')	
	else:
		print('Invalid')

	return HttpResponse(serializer.data)
'''

'''from .serializers import FormSerializer
from .models import Form


@api_view(['GET'])
def formList(request):
	forms = Form.objects.all()
	serializer = FormSerializer(forms, many = True)
	return Response(serializer.data)


@api_view(['GET'])
def formDetail(request, pk):
	form = Form.objects.get(id = pk)
	serializer = FormSerializer(form, many = False)
	return Response(serializer.data)


@api_view(['POST'])
def formCreate(request):
	serializer = FormSerializer(data = request.data)
	
	if serializer.is_valid():
		serializer.save()
	else:
		print(serializer.errors)

	return Response(serializer.data)

@api_view(['GET', 'DELETE'])
def formDelete(request, pk):
	try:
		row = Form.objects.get(id = pk)

	except Exception as e:
		print(e)

	else:
		row.delete()

	return Response(200)

@api_view(['PUT'])
def formUpdate(request, pk):
	try:
		row = Form.objects.get(id = pk)

	except Exception as e:
		print(e)

	else:
		serializer = FormSerializer(row, many = False)
		
		serializer.data
		

	return Response(200)'''