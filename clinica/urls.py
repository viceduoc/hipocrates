from django.urls import path
from .views import home, reserva

urlpatterns = [
    path('', home, name = "home"),
    path('reserva.html', reserva, name="reserva"),


]