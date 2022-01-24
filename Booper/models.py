from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Post(models.Model):
  titulo = models.CharField(max_length=250)
  slug = models.CharField(max_length=250)
  autor = models.ForeignKey(User, on_delete=models.CASCADE)

  def __str__(self):
      return self.titulo

class SiteUser(models.Model):
  slug = models.SlugField(max_length=250)
  username = models.CharField(max_length=30)
  email = models.EmailField()
  password = models.CharField(max_length=30)

  def __str__(self):
    return self.username

class Arquivo(models.Model):
  arquivo = models.FileField(upload_to="Booper", blank=True, null=True)