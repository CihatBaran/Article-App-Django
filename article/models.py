from django.db import models
from ckeditor.fields import RichTextField
# Create your models here.


class Article(models.Model):
    author = models.ForeignKey("auth.User", on_delete=models.CASCADE,
                               verbose_name="Name of the author")
    title = models.CharField(max_length=50,
                             verbose_name="title is related with ")
    # content = models.TextField()
    content = RichTextField()
    article_image = models.FileField(
        blank=True, null=True, verbose_name="Add picture to Article")
    created_date = models.DateTimeField(
        auto_now_add=True, null=True, verbose_name="Add picture to article")

    def __str__(self):
        return self.title
