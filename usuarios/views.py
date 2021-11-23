from django.http import request
from django.shortcuts import redirect, render , get_object_or_404
from django.contrib.auth.models import User
from django.contrib import auth, messages
from pessoa.models import Pessoa
from django.contrib.auth import logout

# Create your views here.

def cadastro(request):
    if request.method == 'POST':
        nome = request.POST['nome']
        email = request.POST['email']
        senha = request.POST['password']
        senha2 = request.POST['password2']

        if campo_vazio(nome):
            messages.error(request,'O campo nome nao pode ficar em branco!')
            return redirect('cadastro')
        if campo_vazio(email):
            messages.error(request,'O campo email nao pode ficar em branco!')
            return redirect('cadastro')
        if senhas_nao_sao_iguais(senha, senha2):
            messages.error(request, 'As senhas nao sao iguais') 
            return redirect('cadastro')
        if User.objects.filter(email=email).exists():
            messages.error(request,'Usuario ja cadastrado')
            return redirect('cadastro')
        if User.objects.filter(username=nome).exists():
            messages.error(request,'Usuario ja cadastrado')
            return redirect('cadastro')
        user = User.objects.create_user(username=nome, email=email, password=senha) 
        user.save()
        messages.success(request, 'Cadastro realizado com sucesso')    
        return redirect('login')

    else:    
        return render(request, 'usuarios/cadastro.html')

def login(request):
    if request.method == 'POST':
        email = request.POST['email']
        senha = request.POST['senha']
        if campo_vazio(email) or campo_vazio(senha) == "":
            messages.error(request,'Os campos email e senha nao podem ficar em branco')
            return redirect('login')
        print(email,senha)
        if User.objects.filter(email=email).exists():
            nome = User.objects.filter(email=email).values_list('username', flat=True).get()
            user = auth.authenticate(request, username=nome, password=senha)
            if user is not None:
                auth.login(request ,user)
                print('Login realizado com sucesso')
                return redirect('dashboard')
    return render(request, 'usuarios/login.html')

def logout(request):
    auth.logout(request)
    return redirect('index')

def dashboard(request):
    if request.user.is_authenticated:
        id = request.user.id
        pessoas = Pessoa.objects.order_by('nome').filter(pessoa=id)
        dados = {
            'pessoas' : pessoas
        }

        return render(request,'usuarios/dashboard.html')
    else:
        return redirect('index')

def cadastra_pessoa(request):    
    if request.method == 'POST':
        nome = request.POST['nome']  
        user = get_object_or_404(User, pk=request.user.id)
        pessoa = Pessoa.objects.create(pessoa=user,nome=nome)   
        pessoa.save()
        return redirect('dashboard')
    else:
        return render(request, 'usuarios/cria_pessoa.html')

def campo_vazio(nome):
    return not nome.strip()

def senhas_nao_sao_iguais(senha,senha2):
    senha != senha2