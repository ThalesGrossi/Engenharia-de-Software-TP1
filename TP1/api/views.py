from django.shortcuts import redirect, render
from .forms import RegistroUsuario
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from .decorators import unauthorized_user
# Create your views here.

def main(request):
    return render(request, 'usuario/base.html')

def home(request):
    return render(request, 'usuario/index.html')

@unauthorized_user
def formDeRegistro(request):
    form = RegistroUsuario()
    if request.method=='POST':
        form=RegistroUsuario(request.POST)
        if form.is_valid():
            form.save()
            username=form.cleaned_data.get('username')
            messages.info(request, username+' ,sua conta foi criada. Faça login para continuar.')
            redirect()
    context = {'form':form}
    return render(request,'usuario/registro.html', context)

@unauthorized_user
def formDeLogin(request):
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('somewhere')
        else:
            messages.info(request,'Usuário ou senha estão incorretos')
    return render(request,'usuario/login.html')

def formDeLogout(request):
    logout(request)
    return render(request,'usuario/index.html')

@login_required(login_url='usuario:Login')
def perfil(request):
    return render(request,'usuario/perfil.html')

