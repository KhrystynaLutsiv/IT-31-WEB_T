from django.db import models

class Articles(models.Model):
    title = models.CharField('Назва', max_length=50)
    anons = models.CharField('Анонс', max_length=50)
    full_text = models.TextField('Текст')
    date = models.DateTimeField('Дата публікації')

    def __str__(self):
        return self.title