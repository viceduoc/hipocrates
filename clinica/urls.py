from django.urls import path
from .views import home, reserva, crearreserva, verreserva

urlpatterns = [
    path('', home, name = "home"),
    path('reserva.html', reserva, name="reserva"),
    path('crear-reserva.html', crearreserva, name="crear-reserva"),
    path('ver-reservas.html', verreserva, name="ver-reserva"),
    


]