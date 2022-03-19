from django.db import models
from django.urls import reverse

class News(models.Model):
    header = models.CharField('Заголовок',max_length=200)
    date_published = models.DateTimeField(auto_now_add=True)
    body = models.TextField('Содержание', max_length=10000)
    image = models.ImageField("Изображение", upload_to = 'images/', null = True)

    def __str__(self) -> str:
        return str(self.header)

    def get_absolute_url(self):
        return reverse('news-detail', args=[str(self.id)])

    def show_short_text(self):
        return str(self.body)[:1000]

    class Meta:
        ordering = ['date_published']
    

