from dataclasses import field
from pyexpat import model
from telnetlib import LOGOUT
from unicodedata import name
from django.urls import reverse
from django.shortcuts import render

from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView
from django.contrib.auth.decorators import login_required
from django import forms

from . models import Post, SiteUser, Arquivo

# Create your views here.
variavel = 1
def index(request):
  return render(request, "Booper/index.html")


def entrar(request):
  return render(request, "Booper/entrar.html")
  
def sair(request):
    LOGOUT(request)

def generos(request):
  return render(request, "Booper/generos.html")

def leitura(request):
  # context = { Envio de variáveis por aq. Poderoso, mas bem específico
  #   'algo': 1,
  # }
  return render(request, "Booper/leitura.html")

class PostListView(ListView): #criando uma ListView, q é uma View com acesso à listagem do BD
  model = Post
  template_name = "Booper/leitura.html"
  context_object_name = "minhaLista"

class PostDetailView(DetailView):
  model = Post
  template_name = "Booper/PostEspecifico.html"
  context_object_name = "post"

class CadastroFormView(CreateView):
  model = SiteUser
  template_name = "Booper/cadastro.html"
  fields = ["username", "email", "password"]

  def get_success_url(self):
    return reverse('index')

# class UploadFileForm(forms.Form):
#   model = Arquivo
#   template_name = "Booper/index.html"
#   fields = ["arquivo-upload"]
#   title = forms.CharField(max_length=50)
#   file  = forms.FileField()

#   def get_success_url(self):
#     return reverse("leitura")