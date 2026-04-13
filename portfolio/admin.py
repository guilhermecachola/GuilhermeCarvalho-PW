from django.contrib import admin

# Register your models here.

class Licenciatura(models.Model):
    nome = models.CharField(max_length=100)
    apresentacao = models.TextField()
    objetivos = models.TextField()
    link_deisi = models.URLField(blank=True)

    def __str__(self):
        return self.nome


class Docente(models.Model):
    nome = models.CharField(max_length=100)
    link_lusofona = models.URLField()

    def __str__(self):
        return self.nome

class UnidadeCurricular(models.Model):
    nome = models.CharField(max_length=100)
    ano = models.IntegerField()
    semestre = models.IntegerField()
    ects = models.IntegerField()
    imagem = models.ImageField(upload_to='ucs/', blank=True)
    docentes = models.ManyToManyField(Docente, related_name='ucs')
    licenciatura = models.ForeignKey(Licenciatura, on_delete=models.CASCADE, related_name='ucs')

    def __str__(self):
        return self.nome

class Tecnologia(models.Model):
    nome = models.CharField(max_length=50)
    logo = models.ImageField(upload_to='tecnologias/', blank=True)
    link_oficial = models.URLField()
    descricao = models.TextField()
    nivel_interesse = models.IntegerField(help_text="Escala de 1 a 5")

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