from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Forum
from .forms import ForumForm


def index(request):
	return render(request, "index.html")

@login_required
def perfil(request):
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
	resposta = Forum.objects.all()
	contexto = {
		'lista_perguntas': resposta
	}
	return render(request, 'perfil.html', contexto)

def cadastrar_pergunta(request):
	if request.POST:
		form = ForumForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('pergunta_listar')
	else:
		form ForumForm()
		contexto = {
			'form' : form
		}
	
	return render(request, 'perfil.html', contexto)


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

# Create your views here.
