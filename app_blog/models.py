from django.db import models

# Create your models here.
class Post(models.Model):
    titulo = models.CharField(max_length=200)
    conteudo = models.TextField()
    publicado_em = models.DateTimeField(auto_now_add=True)
    autor = models.CharField(max_length=100)
    resumo = models.TextField()
    slug = models.SlugField()
    img_url = models.TextField()

    class Meta:
        ordering = ['-publicado_em']

class Comentario(models.Model):
    post = models.ForeignKey(Post, related_name='comentarios', on_delete=models.CASCADE)#como post é FK é possivel fazer a ligação
    nome = models.CharField(max_length=150)
    email = models.EmailField()
    conteudo = models.CharField(max_length=500)
    publicado_em = models.DateTimeField(auto_now_add=True)

    class Meta:
     ordering = ['-publicado_em']