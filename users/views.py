from django.shortcuts import render
from django.views.generic import TemplateView

from common.views import CommonMixin


# Create your views here.
class SignUpView(CommonMixin, TemplateView):
    template_name = 'users/signup.html'
    title = 'Registration'
