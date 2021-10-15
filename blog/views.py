#from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView,UpdateView
from . models import Post

class BlogListView(ListView):
    model = Post
    template_name = 'blog/home.html'

class BlogDetailView(DetailView):
    model = Post
    template_name = 'blog/post_detail.html'
    # context_object_name = 'custom'

class BlogCreateView(CreateView):
    model = Post
    template_name = 'blog/post_new.html'
    # fields = '__all__'
    fields = ('autor', 'titulo','conteudo')

class BlogUpdateView(UpdateView):
    model = Post
    template_name = 'blog/post_edit.html'
    # fields = '__all__'
    fields = ('titulo','conteudo')
