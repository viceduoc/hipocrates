from django.shortcuts import render,HttpResponse


# Create your views here.


def home(request):
    return render(request, 'clinica/home.html')


def prueba(request):
    contexto = {
        "especialidad": "Medicina general"
    }
    return render(request, 'template/clinica/home.html', contexto)

def test(request):
    lista=[ "Lasaña", "Porotos"]
    contexto = {"especialidad": "Medicina general", "comidas": lista}
    return render(request, 'template/clinica/home.html', contexto)