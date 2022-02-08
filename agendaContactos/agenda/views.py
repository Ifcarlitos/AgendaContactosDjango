from math import remainder
from pickletools import read_uint1
from unicodedata import name
from django.shortcuts import redirect, render
from django.http import HttpResponse
from .models import contacto
from .forms import contactoForm
# Create your views here.

def inicio(request):
    return HttpResponse("hola")

def index(request):
    contactos = contacto.objects.all()
    #print(contactos)
    return render(request, 'paginas/index.html', {'contactos': contactos})

def crea(request):
    formulario = contactoForm(request.POST or None)
    if formulario.is_valid():
        formulario.save()
        return redirect('index')
    return render(request, 'paginas/crea.html', {'formulario': formulario})

def editar(request, id):
    contactoEdit = contacto.objects.get(id=id)
    formulario = contactoForm(request.POST or None, instance=contactoEdit)
    if formulario.is_valid() and request.method == 'POST':
        formulario.save()
        return redirect('index')
    return render(request, 'paginas/editar.html',  {'formulario': formulario})

def eliminar(request, id):
    contactoDelete = contacto.objects.get(id=id)
    contactoDelete.delete()
    return redirect('index')

def busqueda(request):
    return render(request, 'paginas/busqueda.html')

def buscar(request):
    mensaje = request.GET["textbusqueda"]
    option = request.GET["options"]
    #print(option)
    if(option == 'on'):
        print("soy nombre")
        contactos = contacto.objects.filter(nombre = mensaje)
        print(contactos)
    elif(option == 'off'):
        print("soy telefono")
        contactos = contacto.objects.filter(telefono = mensaje)
    else:
        contactos =contacto.objects.all()

    #print(mensaje)
    #print(contactos)
    return render(request, 'paginas/mostrarbusqueda.html', {'contactos': contactos})
    #return HttpResponse('buenas')