from django.shortcuts import render


def categoria_list(request):
    MAX_OBJECTS = 20
    cat = Categoria.objects.all()[:MAX_OBJECTS]
    data = {"result":list(cat.values("descripcion","activo"))}
    return jsonResponse(data)

def categoria_detalle(request,pk):
    pass
