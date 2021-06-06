from django.db import models


class Generator(models.Model):
    title = models.CharField('Название', max_length=50)
    task = models.TextField('Действия')
    tasks_list = task.__str__().split(',')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Генератор'
        verbose_name_plural = 'Генераторы'
