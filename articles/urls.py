from django.urls import path
from .views import ArticleList, ArticleDetail

app_name = 'articles'

urlpatterns = [
    path('', ArticleList.as_view(), name='article-list'),
    path('<slug:slug>/', ArticleDetail.as_view(), name='article-detail')
]
