from django.db import models


class Genre(models.Model):

    name = models.CharField(max_length=256, verbose_name='Название')

    class Meta:
        verbose_name = 'Жанр'
        verbose_name_plural = 'Жанры'

    def __str__(self):
        return self.name


class Author(models.Model):

    name = models.CharField(max_length=256, verbose_name='Имя')
    phone = models.CharField(max_length=256, verbose_name='Телефон')

    class Meta:
        verbose_name = 'Автор'
        verbose_name_plural = 'Авторы'

    def __str__(self):
        return self.name


class Article(models.Model):

    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    genre = models.ManyToManyField(Genre, through='Articleship')
    title = models.CharField(max_length=256, verbose_name='Название')
    text = models.TextField(verbose_name='Текст')
    published_at = models.DateTimeField(verbose_name='Дата публикации')
    image = models.ImageField(null=True, blank=True, verbose_name='Изображение',)


    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'

    def __str__(self):
        return self.title


class Articleship(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE, verbose_name='Статья', related_name='scopes')
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE, verbose_name='Жанр', related_name='scopes')
    is_main = models.BooleanField(verbose_name='Основной')

    class Meta:
        verbose_name = 'Жанр статьи'
        verbose_name_plural = 'Жанры статьи'
        ordering = ('-is_main', 'genre__name')

    def __str__(self):
        return f'{self.article}_{self.genre}'