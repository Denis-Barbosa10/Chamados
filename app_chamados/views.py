from django.http import HttpResponse, Http404
from django.shortcuts import render
from .models import Chamado




def chamado_resumo_template(request):
    total = Chamado.objects.count()
    return render(request, 'app_chamados/resumo.html', {'total': total, 'bola': 'teste'})


def chamado_detalhe(request,chamado_id):
	if request.user.is_superuser:
		try:
			chamado = Chamado.objects.get(pk=chamado_id)
		except Exception:
			raise Http404("Página não encontrada")

		return render(request, 'app_chamados/detalhe.html', {'chamado': chamado})
	else:
		return HttpResponse('Você não está autorizado a visualizar essa pagina. <a href= "/conta/login">Faça Login aqui</a>')

def pagina_inicial(request):
    chamados = Chamado.objects.all()
    return render(request, 'app_chamados/inicial.html', {'todas_chamados': chamados})