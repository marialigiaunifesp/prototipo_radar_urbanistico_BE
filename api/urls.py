from django.urls import path, include
from . import views

urlpatterns = [
	path('form-create/', views.formCreate, name = "form-create"),
	path('get-sicar/', views.getSicar, name = "get-sicar"),
	path('form-create-file/', views.formFile, name = 'form-create-file')
]