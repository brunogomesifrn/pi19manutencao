from django.forms import ModelForm
from .models import Forum, Agendamento, Servico

class ForumForm(ModelForm):
	class Meta():
		model = Forum
		fields = ['pergunta', 'resposta']


class AgendamentoForm(ModelForm):
	class Meta:
		model = Agendamento
		fields = ['horario']


class ServicoForm(ModelForm):
	class Meta:
		model = Servico
		fields = ['descricao', 'preco']
