from django.urls import path

from eventos.views import Evento


app_name = 'eventos'


urlpatterns = [
    path('<int:id>', Evento, name='Evento'),
]