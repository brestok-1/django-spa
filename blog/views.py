from django.shortcuts import render
from django.views.generic import TemplateView

from blog.common.views import CommonMixin


# Create your views here.
class IndexView(CommonMixin, TemplateView):
    template_name = 'blog/index.html'
    title = 'Добро пожаловать!'
