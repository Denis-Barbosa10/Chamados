from django.urls import path

from .views import chamado_resumo_template,chamado_detalhe,pagina_inicial

urlpatterns = [
	path('resumo', chamado_resumo_template, name='resumo'),
	path('detalhe/<int:chamado_id>/', chamado_detalhe, name='detalhe'),
	
	path('', pagina_inicial, name='inicio')
]