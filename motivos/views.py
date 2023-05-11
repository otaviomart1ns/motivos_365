from django.shortcuts import render
from motivos.models import Bilhete


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
