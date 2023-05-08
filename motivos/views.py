from django.contrib.auth import authenticate, login
from django.shortcuts import render
from django.http import HttpResponseRedirect

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect('/')
        else:
            error = "Usuário ou senha incorretos"
            return render(request, 'registration/login.html', {'error': error})
    else:
        return render(request, 'registration/login.html')
    
def index(request):
        return render(request, 'motivos/index.html')
