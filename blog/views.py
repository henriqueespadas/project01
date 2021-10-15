#from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView,DetailView,UpdateView,DeleteView
from django.views.generic import CreateView
from .models import Post


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


class BlogDeleteView(DeleteView):
    model = Post
    template_name = 'blog/post_delete.html'
    # fields = '__all__'
    success_url = reverse_lazy('home')

