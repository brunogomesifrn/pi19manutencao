from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Forum, Servico, Agendamento
from .forms import ForumForm, AgendamentoForm, ServicoForm


def index(request):
    return render(request, "index.html")

@login_required
def perfil(request):
    pergunta = Forum.objects.all()
    contexto = {
        'lista_forum': pergunta
    }
    return render(request, 'perfil.html', contexto)

    if User.is_superuser==1:
        return render(request, "perfiladmin.html")
    else:
        return render(request, "perfil.html")

def cadastro(request):
    form = UserCreationForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('login')
    contexto = {
        'form': form
    }
    return render(request, 'cadastro.html', contexto)

#aqui eu não tenho certeza, tô vendo uns vídeos, mas não deu certo tudo

def pergunta_listar(request, id):
    pergunta = Forum.objects.all()
    contexto = {
        'lista_forum': pergunta
    }
    return render(request, 'perfil.html', contexto)

def cadastrar_pergunta(request):
    if request.POST:
        form = ForumForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('perfil')
    else:
        form = ForumForm()
    
    contexto = {
            'form' : form
        }
    
    return render(request, 'cadastrar_pergunta.html', contexto)


# vai ate aqui em cima
@login_required
def dados(request, id):
    user = User.objects.get(pk=id)
    form = UserCreationForm(request.POST or None, instance=user)
    if form.is_valid():
        form.save()
        return redirect('perfil')
    contexto = {
        'form': form
    }
    return render(request, 'cadastro.html', contexto)


def editar(request, id):
    responder = Forum.objects.get(pk=id)
    form = ForumForm(request.POST or None, request.FILES or None, instance = forum)
    if form.is_valid():
        form.save()
        return redirect('perfil')
    contexto = {
        'form' : form
    }
    return render(request, 'cadastrar_pergunta.html', contexto)

def apagar(request, id):
    apagar = Forum.objects.get(pk=id)
    apagar.delete()
    return redirect('perfil')


@login_required
def agendar(request):
    servicos = Servico.objects.all()
    contexto = {
        'servicos': servicos
    }
    return render(request, 'agendar.html', contexto)


@login_required
def agendar_servico(request, id):
    servico = Servico.objects.get(pk=id)
    form = AgendamentoForm(request.POST or None, instance=Agendamento(cliente=request.user, servico=servico))
    if form.is_valid():
        form.save()
        return redirect('agendamentos')
    contexto = {
        'servico': servico,
        'form': form,
    }
    return render(request, 'agendar_servico.html', contexto)


@login_required
def agendamentos(request):
    agendamentos = (
        Agendamento.objects.all()
        if request.user.is_superuser
        else Agendamento.objects.filter(cliente=request.user)
    )
    contexto = {
        'agendamentos': agendamentos
    }
    return (
        render(request, 'agendamentos.html', contexto)
        if request.user.is_superuser
        else render(request, 'meus_agendamentos.html', contexto)
    )


@login_required
def cadastrar_servico(request):
    if not request.user.is_superuser:
        return redirect('perfil')
    if request.POST:
        form = ServicoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('agendamentos')
    else:
        form = ServicoForm()
    contexto = {
        'form' : form
    }
    return render(request, 'cadastrar_servico.html', contexto)



def problema1(request):
    return render(request, "problema1.html")

def problema2(request):
    return render(request, "problema2.html")

def problema3(request):
    return render(request, "problema3.html")

def problema4(request):
    return render(request, "problema4.html")

def problema5(request):
    return render(request, "problema5.html")

def problema6(request):
    return render(request, "problema6.html")

def paginatexte(request):
    return render(request, "paginatexte.html")

# Create your views here.
