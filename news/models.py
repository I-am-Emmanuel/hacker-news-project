from django.db import models

# Create your models here.

class NewsItem(models.Model):
    title = models.CharField(max_length=200, unique=True)
    url = models.URLField(blank=True)
    points = models.PositiveIntegerField(default=0)
    author = models.CharField(max_length=15)
    added_through_api = models.BooleanField(default=False)
    comments = models.URLField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now=True)
    


    def __str__(self):
        return f'{self.title} {self.url} {self.vote}'

    class Meta:
        ordering = ('-created_at',)
