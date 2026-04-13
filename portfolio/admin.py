from django.contrib import admin

# Register your models here.

class Licenciatura(models.Model):
    nome = models.CharField(max_length=100)
    apresentacao = models.TextField()
    objetivos = models.TextField()
    link_deisi = models.URLField(blank=True)

    def __str__(self):
        return self.nome