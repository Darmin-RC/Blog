from django.shortcuts import render
from django.views.generic import TemplateView, DetailView

from .models import Post

class BlogHomePageView(TemplateView):
    template_name = "blog/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["posts"] = Post.objects.all()
        return context

class PostDetailView(DetailView):
    model = Post
    template_name = 'blog/post-detail.html'
    context_object_name = 'post'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Cambié filter por get y asigné el objeto al contexto
        post = Post.objects.get(slug=self.kwargs.get('slug'))
        context["post"] = post
        return context
