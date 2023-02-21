import re

from django.db.models import Q
from django.http import HttpResponseRedirect
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import TemplateView, ListView, DetailView, CreateView, FormView

from blog.forms import CommentForm, ContactForm
from blog.models import Article, Comment
from common.views import CommonMixin
from blog.tasks import send_feedback

# Create your views here.
class IndexView(CommonMixin, ListView):
    template_name = 'blog/index.html'
    title = 'Добро пожаловать!'
    model = Article
    paginate_by = 6


class ArticleView(DetailView):
    template_name = 'blog/one-project.html'
    slug_url_kwarg = 'article_slug'
    model = Article

    def get_context_data(self, **kwargs):
        context = super(ArticleView, self).get_context_data(**kwargs)
        context['title'] = f'Article : {self.object.title}'
        recent_article = Article.objects.all()[:5]
        if self.object.id in map(lambda x: x.id, recent_article):
            final_article = Article.objects.filter(~Q(id=self.object.id))[:5]
        else:
            final_article = recent_article[:5]
        context['recent_articles'] = final_article
        context['form'] = CommentForm(self.request.POST)
        context['comments'] = Comment.objects.filter(post__slug=self.object.slug)
        return context


class SearchView(CommonMixin, ListView):
    title = 'Search result'
    template_name = 'blog/search.html'
    model = Article
    paginate_by = 6

    # def get(self, *args, **kwargs):
    #     if self.request.GET.get('q'):
    #         if re.sub(r' ', '', self.request.GET.get('q')) == '':
    #             return redirect(self.request.META['HTTP_REFERER'])
    #         else:
    #             return super(SearchView, self).get(self, *args, **kwargs)
    #     else:
    #         return super(SearchView, self).get(self, *args, **kwargs)

    def get_queryset(self):
        query = self.request.GET.get('q')
        result = ''
        if query:
            result = Article.objects.filter(
                Q(h1__icontains=query) | Q(content__icontains=query))
        return result

    def get_context_data(self, **kwargs):
        context = super(SearchView, self).get_context_data(**kwargs)
        context['count'] = len(self.object_list)
        return context


class CommentView(CreateView):
    template_name = 'blog/one-project.html'
    form_class = CommentForm

    def get_success_url(self):
        return redirect(self.request.META['HTTP_REFERER'])

    def post(self, *args, **kwargs):
        form = CommentForm(self.request.POST)
        if form.is_valid():
            slug = re.findall(r'((?:[a-z]+-?)+)\/(?<=$)', self.request.META['HTTP_REFERER'])[0]
            comment = Comment.objects.create(post=Article.objects.get(slug=slug), username=self.request.user,
                                             text=self.request.POST['text'])
            return HttpResponseRedirect(self.request.META['HTTP_REFERER'])
        return super(CommentView, self).post(self, form, *args, **kwargs)


class ContactView(CommonMixin, FormView):
    title = 'Contacts'
    template_name = 'blog/contact.html'
    form_class = ContactForm
    success_url = reverse_lazy('blog:index')

    def post(self, request, *args, **kwargs):
        form = ContactForm(request.POST)
        if form.is_valid():
            send_feedback.delay(form.cleaned_data)
        return super(ContactView, self).post(self, request, *args, **kwargs)