from django.urls import path, include
from . import views

urlpatterns = [
	path('form-create/', views.formCreate, name = "form-create"),
	# path('map-create/', views.mapCreate, name = "map-create")

]
'''
urlpatterns = [
	path('form-create/', views.formCreate, name = "form-create"),
	path('form-list/', views.formList, name = "form-list"),
	path('form-detail/<str:pk>/', views.formDetail, name = "form-detail"),
	path('form-delete/<str:pk>/', views.formDelete, name = "form-delete"),
	
]
'''