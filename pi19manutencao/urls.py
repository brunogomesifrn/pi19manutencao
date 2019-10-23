"""pi19manutencao URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from core.views import index, perfil, cadastro, dados, pergunta_listar, cadastrar_pergunta, editar, apagar, problema1, problema2, problema3
from django.contrib.auth import views as auth_views

urlpatterns = [

    path('problema1/', problema1, name='problema1'),
    path('problema2/', problema2, name='problema2'),
    path('problema3/', problema3, name='problema3'),
    path('apagar/<int:id>', apagar, name='apagar'),
    path('editar/<int:id>', editar, name='editar'),
    path('cadastrar_pergunta', cadastrar_pergunta, name='cadastrar_pergunta'),
    path('pergunta', pergunta_listar, name='pergunta'),
	path('', index, name='index'),
	path('perfil/', perfil, name='perfil'),
	path('cadastro/', cadastro, name='cadastro'),
	path('dados/<int:id>/', dados, name='dados'),
	path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('admin/', admin.site.urls),
]
