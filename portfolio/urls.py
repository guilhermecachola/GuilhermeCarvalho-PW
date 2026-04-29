urlpatterns = [
    path('', views.tecnologias_view, name='home'),
    # Tecnologias
    path('tecnologias/', views.tecnologias_view, name='tecnologias'),
    path('tecnologia/nova/', views.nova_tecnologia, name='nova_tecnologia'),
    path('tecnologia/<int:id>/editar/', views.edita_tecnologia, name='edita_tecnologia'),
    path('tecnologia/<int:id>/apagar/', views.apaga_tecnologia, name='apaga_tecnologia'),

    # Competências
    path('competencias/', views.competencias_view, name='competencias'),
    path('competencia/nova/', views.nova_competencia, name='nova_competencia'),
    path('competencia/<int:id>/editar/', views.edita_competencia, name='edita_competencia'),

    # Formações
    path('formacoes/', views.formacoes_view, name='formacoes'),
    path('formacao/nova/', views.nova_formacao, name='nova_formacao'),
    path('formacao/<int:id>/editar/', views.edita_formacao, name='edita_formacao'),
]