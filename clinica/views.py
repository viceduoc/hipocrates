from django.shortcuts import render


# Create your views here.


def home(request):
    lista = [ "Lasaña", "Porotos", "Lentejas"]
    gui = {
        "home":"Esta en Home",
        "especialidad": "Medicina general", 
        "comidas": lista
        }
    
    return render(request, 'clinica/home.html',gui)

 

def reserva(request):
    lista = [
         "Lasaña", "Porotos", "Lentejas"
         ]
    gui = {
        "reserva":"Esta en Reserva de horas",
        "especialidad": "Medicina general",
        "comidas": lista
     }
    return render(request, 'clinica/reserva.html', gui)

    
def crearreserva(request):
    lista = [ "Lasaña", "Porotos", "Lentejas"]
    gui = {
        "home":"Esta en Home",
        "especialidad": "Medicina general", 
        "comidas": lista
        }
    
    return render(request, 'clinica/crear-reserva.html',gui)

