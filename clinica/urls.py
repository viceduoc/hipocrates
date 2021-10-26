from django.urls import path
from .views import home, reserva, crearreserva

urlpatterns = [
    path('', home, name = "home"),
    path('reserva.html', reserva, name="reserva"),
    path('crear-reserva.html', crearreserva, name="crear-reserva"),


]