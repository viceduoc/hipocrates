from django.shortcuts import render


# Create your views here.


def home(request):
    contexto = {
        "especialidad": "Medicina general"
    }
    return render(request, 'clinica/home.html',contexto)

  







def test(request):
    lista = [ "Lasaña", "Porotos", "Lentejas"]
    contexto = {"especialidad": "Medicina general", "comidas": lista}
    return render(request, 'template/clinica/home.html', contexto)



def reserva(request):
    return render(request, 'clinica/reserva.html')