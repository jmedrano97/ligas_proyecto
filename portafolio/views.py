from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.shortcuts import redirect
# Create your views here.
from miliga.forms import *
def portafolio(request):
    context = {}
    context['form'] = ContactoForm()
    context = comprobar_mensajes(request, context)
    return render(request, 'portafolio/portafolio.html', context)


def contacto(request):
    print('contacto----------')
    context = {}
    context = comprobar_mensajes(request, context)
    if request.method == 'POST':
        form = ContactoForm(request.POST)
        if form.is_valid():
            form.save()
            mensaje = {'desc':'Mensaje enviado correctamente', 'tipo':'success'}
            request.session['mensaje'] = mensaje
            return redirect('portafolio:portafolio')
        else:
            mensaje = {'desc':'Error al enviar mensaje', 'tipo':'danger'}
            request.session['mensaje'] = mensaje
            context = comprobar_mensajes(request, context)
            return redirect('portafolio:portafolio')
        
def comprobar_mensajes(request, context):
    if 'mensaje' in request.session:
        context['mensaje'] = request.session.get('mensaje')
        del request.session['mensaje']
    return context