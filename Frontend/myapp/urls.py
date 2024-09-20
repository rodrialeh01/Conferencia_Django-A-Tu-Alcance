from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('carga/', views.mostrar_carga, name='carga'),
    path('cargaxml/', views.cargarXML, name='cargaxml'),
    path('enviarxml/', views.cargarAlBackend, name='enviarxml'),
    path('limpiar/', views.limpiar, name='limpiar'),
    path('lenguajes/', views.verLenguajes, name='lenguajes'),
    path('top/',views.verTop,name='top'),
    path('pdf/', views.verPDF, name='pdf')
]