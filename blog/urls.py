from django.urls import path
from blog.views import IndexView, ArticleView, SearchView

app_name = 'blog'

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('article/<slug:article_slug>/', ArticleView.as_view(), name='one_project'),
    path('search/', SearchView.as_view(), name='search')
]
