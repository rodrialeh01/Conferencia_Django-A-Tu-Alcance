import requests
from django.contrib import messages
from django.shortcuts import render

from .forms import FileForm

# Create your views here.

endpoint = 'http://localhost:5000/'

def index(request):
    return render(request, 'index.html')

def mostrar_carga(request):
    ctx = {
        'title': 'Carga Masiva'
    }
    return render(request, 'cargaxml.html', ctx)

contexto = {
    'contenido_archivo':None,
    'binario_xml':None
}

def cargarXML(request):
    ctx = {
        'contenido_archivo': None
    }
    try:
        if request.method == 'POST':
            #obtenemos el formulario
            form = FileForm(request.POST, request.FILES)
            #verificamos si el formulario es valido
            if form.is_valid():
                #obtenemos el archivo
                archivo = request.FILES['file']
                #guardamos el binario
                xml = archivo.read()
                xml_decodificado = xml.decode('utf-8')
                #guardamos el contenido del archivo
                contexto['binario_xml'] = xml
                contexto['contenido_archivo'] = xml_decodificado
                ctx['contenido_archivo'] = xml_decodificado
                return render(request, 'cargaxml.html',ctx)
    except:
        return render(request, 'cargaxml.html')
    
def cargarAlBackend(request):
    try:
        if request.method == 'POST':
            xml = contexto['binario_xml']
            if xml is None:
                messages.error(request, 'No se ha cargado ningun archivo')
                return render(request, 'cargaxml.html')

            #PETICION AL BACKEND
            url = endpoint + 'lenguaje/cargar'
            respuesta = requests.post(url, data=xml)
            mensaje = respuesta.json()
            if respuesta.status_code == 200:
                messages.success(request, mensaje['message'])
            else:
                messages.error(request, mensaje['message'])
            #Limpiamos el contexto
            contexto['binario_xml'] = None
            contexto['contenido_archivo'] = None
            return render(request, 'cargaxml.html',contexto)

    except:
        return render(request, 'cargaxml.html')
    
def limpiar(request):
    contexto['binario_xml'] = None
    contexto['contenido_archivo'] = None
    return render(request, 'cargaxml.html',contexto)

def verLenguajes(request):
    ctx = {
        'lenguajes': None,
        'title': 'Lenguajes'
    }
    url = endpoint + 'lenguaje/verLenguajes'
    respuesta = requests.get(url)
    data = respuesta.json()
    if respuesta.status_code == 200:
        ctx['lenguajes'] = data['lenguajes']
    return render(request, 'lenguajes.html', ctx)

def verTop(request):
    ctx = {
        'title': 'Top'
    }
    return render(request, 'topLenguajes.html', ctx)

def verPDF(request):
    ctx = {
        'title': 'PDF'
    }
    return render(request, 'verPdf.html', ctx)