from django.urls import path

from portafolio.views import portafolio, contacto

app_name = 'portafolio'

urlpatterns = [
    path('', portafolio, name='portafolio'),
    path('contacto/', contacto, name='contacto'),
]