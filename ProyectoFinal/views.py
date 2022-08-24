from contextvars import Context
from pipes import Template
from django.http import HttpResponse
from django.template import Template, Context, loader

# def index(request):
#     with open ("../ProyectoFinal/ProyectoFinal/templates/index.html", "r") as file:
#         home = Template(file.read())
#     contexto = Context()
#     docu = home.render(contexto)

#     return HttpResponse(docu)

def index(request):
    home = loader.get_template('index.html')
    doc = home.render()

    return HttpResponse(doc)

def saludo(request):
	return HttpResponse("Hola Django - Coder")
