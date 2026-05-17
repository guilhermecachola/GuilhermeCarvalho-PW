from django.urls import path
from . import views

app_name = 'artigos'

urlpatterns = [
    path('', views.lista_artigos, name='lista'),
    path('<int:artigo_id>/', views.detalhe_artigo, name='detalhe'),
    path('novo/', views.novo_artigo, name='novo'),
    path('<int:artigo_id>/comentar/', views.novo_comentario, name='comentar'),
    path('<int:artigo_id>/rating/', views.rating_artigo, name='rating'),
]