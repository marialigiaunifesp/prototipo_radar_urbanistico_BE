from django.db import models

# Create your models here.

class Form(models.Model):
	documento = models.CharField(max_length = 70)
	variavel  = models.CharField(max_length = 70)
	valor  = models.CharField(max_length = 70)
	areaAnalise = models.CharField(max_length = 70, blank = True, null = True)
	dataDocumento = models.CharField(max_length = 70)
	referencia = models.CharField(max_length = 70)
	
	def __str__(self):
		return documento
