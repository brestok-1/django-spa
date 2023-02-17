from django.urls import path

from users.views import SignUpView

app_name = 'user'

urlpatterns = [
    path('', SignUpView.as_view(), name='signup'),
]
