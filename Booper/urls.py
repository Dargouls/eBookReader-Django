
from django.urls import path, include
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("cadastro", views.CadastroFormView.as_view(), name="cadastro"),
    path("generos", views.generos, name="generos"),
    path("leitura", views.PostListView.as_view(), name="leitura"), #renderizando a view como ListView
    # path("entrar", views.entrar, name="entrar"),
    path("accounts/", include("django.contrib.auth.urls")),
    path("cadastro", views.sair),
    path("post/<slug:slug>/", views.PostDetailView.as_view(), name="detalhes"), #view para uma coisa
]#tbm pode ser feito com int:pk, se eu quiser usar chave primária