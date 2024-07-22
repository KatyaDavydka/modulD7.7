from django.shortcuts import render
from .models import Post
from django.views.generic import ListView, DetailView
from .filters import PostFilter


class NewsList(ListView):
    model = Post
    ordering = '-post_time'
    template_name = 'post_list.html'
    context_object_name = 'posts'
    paginate_by = 10

    def get_template_names(self):
        if self.request.path == '/news/':
            self.template_name = 'post_list.html'
        elif self.request.path == '/news/search/':
            self.template_name == 'search.html'
        return self.template_name


class NewsDetail(DetailView):
    model = Post
    template_name = 'post_detail.html'
    context_object_name = 'post'

class NewsSearch(ListView):
    model = Post
    ordering = '-post_time'
    template_name = 'search.html'
    context_object_name = 'posts'
    paginate_by = 10

    def get_queryset(self):
        queryset = super().get_queryset()
        self.filterset = PostFilter(self.request.GET, queryset=queryset)
        return self.filterset.qs

   def get_context_data(self, **kwargs):
       context = super().get_context_data(**kwargs)
       context['filterset'] = self.filterset
       return context
