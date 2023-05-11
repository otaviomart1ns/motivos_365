from django.shortcuts import render
from motivos.models import Bilhete
from django.http import JsonResponse
from django.db.models import Count
from django.contrib.sessions.backends.db import SessionStore

def login(request):
    return render(request, 'registration/login.html')
    
def index(request):
    context = {}
    if not request.user.last_login:
        try:
            msg = Bilhete.objects.get(pk=1)
            context = {'msg': msg.message}
        except Bilhete.DoesNotExist:
            pass
        

    return render(request, 'motivos/index.html', context)

def message(request):
    session = SessionStore(request.session.session_key)
    first_message = session.get('first_message', True)
    msg = {}
    if first_message:
        first_message = False
        session['first_message'] = first_message
        session.save()
        teste = Bilhete.objects.get(pk=1)
        msg = {'msg': teste.message}
    else:
        message = Bilhete.objects.annotate(num_bilhetes=Count('id') - 1).order_by('?').first()
        msg = {'msg': message.message}
    return JsonResponse(msg)

    
