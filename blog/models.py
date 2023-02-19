from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.timezone import now

from users.models import User


# Create your models here.

class Article(models.Model):
    h1 = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name='URL', default='')
    description = models.TextField(default='')
    content = models.TextField(default='')
    image = models.ImageField(upload_to='article-images')
    time_created = models.DateField()
    author = models.ForeignKey(to=User, on_delete=models.CASCADE)

    def __str__(self):
        return f'Article : {self.title}'

    def get_tags(self):
        return Tags.objects.filter(article__id=self.id)


class Tags(models.Model):
    tag = models.CharField(max_length=120)
    article = models.ForeignKey(to=Article, on_delete=models.CASCADE)

    def __str__(self):
        return 'Tag :' + self.tag

    class Meta:
        verbose_name_plural = 'Tags'
        verbose_name = 'Tag'


class Comment(models.Model):
    post = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='comments')
    username = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_name')
    text = models.TextField()
    created_date = models.DateTimeField(default=now)

    class Meta:
        ordering = ['-created_date']

    def __str__(self):
        return self.text
