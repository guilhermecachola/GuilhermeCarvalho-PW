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