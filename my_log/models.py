from django.db import models

class Article(models.Model):
    title = models.CharField(max_length=255, verbose_name='название')
    content = models.TextField(verbose_name='контент')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Заголовок"
        verbose_name_plural = "Заголовки"


class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE, verbose_name='заголовок')
    author = models.CharField(max_length=100, verbose_name='автор')
    text = models.TextField(verbose_name='содержание')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='дата создания')

    def __str__(self):
        return self.article, self.text

    class Meta:
        verbose_name = "Комментарий"
        verbose_name_plural = "Комментарии"
