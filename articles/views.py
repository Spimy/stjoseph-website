from django.views.generic import ListView, DetailView
from .models import Articles


class ArticleList(ListView):
    template_name = 'articles/article-list.html'
    model = Articles
    paginate_by = 25


class ArticleDetail(DetailView):
    template_name = 'articles/article-detail.html'
    model = Articles
