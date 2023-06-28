from django.urls import path, include
from . import views

urlpatterns = [
	path('form-create/', views.formCreate, name = "form-create"),
	path('coordinate-create/', views.coordinateCreate, name = "coordinate-create"),
	path('get-sicar/', views.getSicar, name = "get-sicar")

]
'''
urlpatterns = [
	path('form-create/', views.formCreate, name = "form-create"),
	path('form-list/', views.formList, name = "form-list"),
	path('form-detail/<str:pk>/', views.formDetail, name = "form-detail"),
	path('form-delete/<str:pk>/', views.formDelete, name = "form-delete"),
	
]
'''