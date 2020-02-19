from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Articles(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField()
    content = models.TextField()
    imageSmall = models.ImageField(default='defaultImageSmall.png', upload_to='articlesPictures/articlesSmall', blank=True)
    image = models.ImageField(default='defaultImage.jpg', upload_to='articlesPictures/articlesImages', blank=True)
    date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, default=None)

    def __str__(self):
        return self.title

    def snippet(self):
        return self.content[:250] + '...'
