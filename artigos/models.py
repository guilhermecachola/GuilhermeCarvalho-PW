from django.db import models
from django.contrib.auth.models import User

class Artigo(models.Model):
    titulo      = models.CharField(max_length=200)
    conteudo    = models.TextField()
    imagem      = models.ImageField(upload_to='artigos/', null=True, blank=True)
    link_externo = models.URLField(max_length=300, null=True, blank=True)
    data_criacao = models.DateTimeField(auto_now_add=True)
    autor       = models.ForeignKey(User, on_delete=models.CASCADE, related_name='meus_artigos')

    def __str__(self):
        return self.titulo

    def media_rating(self):
        ratings = self.ratings.all()
        if ratings.exists():
            return round(sum(r.valor for r in ratings) / ratings.count(), 1)
        return None

class Comentario(models.Model):
    artigo = models.ForeignKey(Artigo, on_delete=models.CASCADE, related_name='comentarios')
    autor  = models.CharField(max_length=100)  # não requer login
    texto  = models.TextField()
    data   = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.autor} → {self.artigo.titulo}"

class Rating(models.Model):
    artigo = models.ForeignKey(Artigo, on_delete=models.CASCADE, related_name='ratings')
    valor  = models.IntegerField()  # 1 a 5
    ip     = models.GenericIPAddressField()
    data   = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('artigo', 'ip')  # um voto por IP por artigo