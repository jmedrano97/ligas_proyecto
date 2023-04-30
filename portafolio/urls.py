from django.urls import path

from portafolio.views import portafolio

app_name = 'portafolio'

urlpatterns = [
    path('', portafolio, name='portafolio'),
]