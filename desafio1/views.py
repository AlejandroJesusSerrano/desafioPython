from django.http import HttpResponse
from django.template import Template, Context, loader

import os

from datetime import datetime

baseroute = 'C:/Users/aleja/OneDrive/Documents/CODER HOUSE/PYTHON/desafio/desafio1/desafio1/'

def template_view(request):
    
    relroute_index = 'templates/index.html'
    
    index_route = os.path.join(baseroute, relroute_index)
    
    index = open(index_route)
    
    templ = Template(index.read())
    
    index.close()

    data = {"name": "Alejandro", "lastname": "Serrano", "date": datetime.now(), "age":38}

    context = Context(data)

    document = templ.render(context)

    return HttpResponse(document)

# def family_view(request):
#     #se define la ruta relativa
#     relroute_family = 'templates/familia.html'
#     #se unifica a la ruta base del scope global
#     index_route = os.path.join(baseroute, relroute_family)
#     #apertura del archivo desde la ruta creada por os    
#     index = open(index_route)
    
#     #template
#     templ = Template(index.read())
    
#     #se cierra el archivo
#     index.close()

#     #captura de datos
#     data = {"relationship": "Padre", "name": "Alejandro", "lastname":  "Bustos Fierro", "date": datetime.now(), "age":86}

#     context = Context(data)

#     document = templ.render(context)

#     return HttpResponse(document)

def view_family_index(request):
    data = {"relationship": "Padre", "name": "Alejandro", "lastname":  "Bustos Fierro", "date": datetime.now(), "age":86}

    template = loader.get_template('familia.html')
    document = template.render(data)

    return HttpResponse(document)
