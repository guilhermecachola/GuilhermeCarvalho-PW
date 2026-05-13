from django.db import models

# Create your models here.



from django.db import models

# Register your models here.




class Docente(models.Model):
    nome = models.CharField(max_length=100)
    link_lusofona = models.URLField()

    def __str__(self):
        return self.nome

# portfolio/models.py

class Licenciatura(models.Model):
    nome = models.CharField(max_length=100)
    apresentacao = models.TextField()
    objetivos = models.TextField()
    competencias = models.TextField(blank=True, null=True) 
    grau = models.CharField(max_length=50, blank=True)    
    link_deisi = models.URLField(blank=True)

    def __str__(self):
        return self.nome

class UnidadeCurricular(models.Model):
    nome = models.CharField(max_length=100)
    codigo = models.IntegerField(unique=True, null=True) 
    ano = models.IntegerField()
    semestre = models.IntegerField()
    ects = models.IntegerField()
    objetivos = models.TextField(blank=True)            
    conteudos = models.TextField(blank=True)            
    imagem = models.ImageField(upload_to='ucs/', blank=True)
    docentes = models.ManyToManyField('Docente', related_name='ucs')
    licenciatura = models.ForeignKey(Licenciatura, on_delete=models.CASCADE, related_name='ucs')

    def __str__(self):
        return self.nome
        
class TipoTecnologia(models.Model):
    nome = models.CharField(max_length=50) # Ex: Frontend, Backend, etc.

    def __str__(self):
        return self.nome

class Tecnologia(models.Model):
    nome = models.CharField(max_length=50)
    tipo = models.ForeignKey(TipoTecnologia, on_delete=models.CASCADE, related_name='tecnologias', null=True, blank=True)    
    logo = models.ImageField(upload_to='tecnologias/', blank=True)
    descricao = models.TextField(help_text="O que faz e o que permite")
    opiniao = models.TextField(help_text="O que gostei ou não", blank=True)
    ink_oficial = models.URLField(blank=True)    
    nivel_interesse = models.IntegerField()

    def __str__(self):
        return self.nome

class Projeto(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField()
    conceitos_aplicados = models.TextField()
    tecnologias = models.ManyToManyField(Tecnologia, related_name='projetos')
    imagem = models.ImageField(upload_to='projetos/', blank=True)
    video_demo = models.URLField(blank=True)
    github_link = models.URLField()
    unidade_curricular = models.ForeignKey(UnidadeCurricular, on_delete=models.CASCADE, related_name='projetos')

    def __str__(self):
        return self.nome

class TFC(models.Model):
    titulo = models.CharField(max_length=200)
    autores = models.CharField(max_length=200)
    ano = models.IntegerField()
    resumo = models.TextField()
    destaque = models.BooleanField(default=False)

    def __str__(self):
        return self.titulo

class Competencia(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField()
    projetos = models.ManyToManyField(Projeto, blank=True, related_name='competencias')

    def __str__(self):
        return self.nome

class Formacao(models.Model):
    titulo = models.CharField(max_length=100)
    instituicao = models.CharField(max_length=100)
    data_inicio = models.DateField()
    data_fim = models.DateField(null=True, blank=True)
    descricao = models.TextField()

    class Meta:
        ordering = ['-data_inicio']

    def __str__(self):
        return self.titulo

class MakingOf(models.Model):
    etapa = models.CharField(max_length=100) 
    data = models.DateField(auto_now_add=True)
    descricao = models.TextField(help_text="Decisões e justificações")
    erros_encontrados = models.TextField(blank=True)
    solucoes = models.TextField(blank=True)
    foto_caderno = models.ImageField(upload_to='makingof/', blank=True)
    uso_ia = models.TextField(blank=True, help_text="Como a IA ajudou nesta etapa")

    def __str__(self):
        return f"{self.etapa} - {self.data}"