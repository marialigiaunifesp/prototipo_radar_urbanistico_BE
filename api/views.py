from django.shortcuts import render


from rest_framework.decorators import api_view
from rest_framework.response import Response

from .serializers import FormSerializer
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
		

	return Response(200)