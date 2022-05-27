from django.shortcuts import render
from django.http import JsonResponse
from .models import *


def categoria_list(request):
    MAX_OBJECTS = 20
    cat = Categoria.objects.all()[:MAX_OBJECTS]
    data = {"result":list(cat.values("id","descripcion","activo"))}
    return JsonResponse(data)

def categoria_detalle(request,pk):
    cat = get_object_or_404(Categoria,pk=pk)
    data = {'results':{'descripcion':cat.descripcion,'activo':cat.activo}}
    return JsonResponse(data)
