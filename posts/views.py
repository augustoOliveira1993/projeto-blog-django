from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.edit import UpdateView
from .models import Post


class PostIndex(ListView):
    model = Post
    template_name = 'posts/index.html'
    paginate_by = 3

class PostBusca(PostIndex):
    pass

class PostCategoria(PostIndex):
    pass

class PostDetalhes(PostIndex):
    pass
