from django.urls import path
from blog.views import IndexView, ArticleView, SearchView
from django.views.decorators.cache import cache_page
app_name = 'blog'

urlpatterns = [
    # path('', cache_page(60)(IndexView.as_view()), name='index'),
    path('', IndexView.as_view(), name='index'),
    path('article/<slug:article_slug>/', ArticleView.as_view(), name='one_project'),
    path('search/', SearchView.as_view(), name='search')
]
