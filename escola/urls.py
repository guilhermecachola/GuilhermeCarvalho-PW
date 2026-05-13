from django.urls import path
from . import views

urlpatterns = [
    path('', views.cursos_view, name="home"),
    path('cursos/', views.cursos_view, name="cursos"),
    path('alunos/', views.alunos_view, name="alunos"),
    path('curso/<int:id>/', views.curso_view, name="curso"),
]