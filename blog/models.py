from django.db import models
#Функция реверс, позволяет переходить по на страницу по названию маршрута.
from django.urls import reverse

class Post(models.Model):
    title = models.CharField(max_length=200, verbose_name='Заголовок')
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE,
     verbose_name='Автор')
    body = models.TextField(verbose_name='Текст')

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'Запись'
        verbose_name_plural = 'Записи'
        ordering = ['title']

  #Определяет какая страница будет загружаться. Будет загружаться индивидуальная страница записи.
    def get_absolute_url(self):
        return reverse('post_detail', args=[str(self.id)])#Выдаёт ошибку, пишет нет такой страницы.
# Create your models here.
