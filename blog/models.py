from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Post(models.Model):
    STATUS = {
        ('rascunho','Rascunho'),
        ('publicado','Publicado'),

    }
    titulo = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250)
    autor = models.ForeignKey(User, on_delete=models.CASCADE)
    conteudo = models.TextField()
    publicado = models.DateTimeField(default=timezone.now)
    criado = models.DateTimeField(auto_now_add=True)
    alterado = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=10, choices=STATUS, default='Rascunho')

    class Meta:
        ordering = ('-publicado',)

    def __str__(self):
        return f'{self.titulo} - {self.slug}'

# Create your models here.
'''
Post.objects.bulk_create([
    Post(titulo='testando o shell do Django- com bulk 2', slug='testando-o-shell-do-django-22',conteudo='Testando o Shell do Django', autor=user),
    Post(titulo='testando o shell do Django- com bulk 3', slug='testando-o-shell-do-django-222',conteudo='Testando o Shell do Django', autor=user),
    Post(titulo='testando o shell do Django- com bulk 44', slug='testando-o-shell-do-django-2244',conteudo='Testando o Shell do Django', autor=user),
])
'''