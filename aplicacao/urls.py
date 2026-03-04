from django.urls import path
from .views import index, contato, produto, cadastrarProduto, salvarProduto, editarProduto, excluirProduto, entrar

urlpatterns = [
    path('', index),
    path('contato', contato, name="urlcontato"),
    path('produto', produto, name="urlproduto"),
    path('cadastrarProduto', cadastrarProduto, name="urlcadastrarProduto"),
    path('salvarProduto', salvarProduto, name="urlsalvarProduto"),
    path('editarProduto/<int:id>', editarProduto, name="urleditarProduto"),
    path('excluirProduto/<int:id>', excluirProduto, name="urlexcluirProduto"),
    path('entrar', entrar, name="urlentrar")
]