from django.contrib.auth.models import User
from django.db import models


class Generator(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Автор', blank=True, null=True)
    title = models.CharField('Название', max_length=50)
    task = models.TextField('Действия')
    tasks_list = task.__str__().split(',')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Генератор'
        verbose_name_plural = 'Генераторы'
