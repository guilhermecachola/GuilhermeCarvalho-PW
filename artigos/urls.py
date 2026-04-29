from django.urls import path
from . import views

app_name = 'artigos'

urlpatterns = [
    path('', views.lista_artigos, name='lista'),
    path('like/<int:artigo_id>/', views.like_artigo, name='like'),
    path('comentar/<int:artigo_id>/', views.novo_comentario, name='comentar'),
]