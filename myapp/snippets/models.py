from django.db import models

from pygments.lexers import get_all_lexers
from pygments.styles import get_all_styles

LEXERS = [item for item in get_all_lexers() if item[1]]
LANGUAGE_CHOICES = sorted([(item[1][0], item[0]) for item in LEXERS])
STYLE_CHOICES = sorted((item, item) for item in get_all_styles())


class Snippet(models.Model):
    title = models.CharField(max_length=100, blank=True, default='')
    code = models.TextField()
    linenos = models.BooleanField(default=False)
    language = models.CharField(
        choices=LANGUAGE_CHOICES, default='python', max_length=100)
    style = models.CharField(
        choices=STYLE_CHOICES, default='friendly', max_length=100)

    class Meta:
        db_table = 'tbl_snipplet'  # Table mapping with exits db.


class Post(models.Model):
    title = models.CharField(max_length=200, blank=True, default='')
    content = models.TextField()
    snipid = models.ForeignKey(
        Snippet,  # Object will be link to.
        db_column='snipid',  # db_column = Foreign Key column name
        on_delete=models.CASCADE)  # Act in case deleted.

    class Meta:
        db_table = 'tbl_post'