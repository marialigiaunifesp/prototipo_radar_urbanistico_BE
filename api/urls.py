from django.urls import path, include
from . import views

urlpatterns = [
	path('form-create/', views.formCreate, name = "form-create"),
	path('get-sicar/', views.getSicar, name = "get-sicar"),
	path('form-post-file/', views.formPostFile, name = 'form-post-file'),
	path('form-get-info/<int:id_sicar>/', views.getInfo, name='get-info'),
	path('form-get-info-api/<int:id_sicar>/', views.DocumentoView.as_view(), name='get-info-api'),
	path('form-get-file/<int:id_arquivo>/', views.download_arquivo, name='download_arquivo'),
]