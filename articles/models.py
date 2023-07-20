from django.db import models
from django.urls import reverse
from django.utils.text import slugify


# Create your models here.
class Articles(models.Model):
    title = models.CharField(verbose_name='موضوع', max_length=200, db_index=True)
    short = models.CharField(verbose_name='توضیح کوتاه', max_length=250)
    text = models.TextField(verbose_name='متن پیام')
    slug = models.SlugField(null=True, blank=True, unique=True, allow_unicode=True)
    image = models.ImageField(upload_to='article', null=True, blank=True,verbose_name='عکس مقاله')
    is_active = models.BooleanField(default=True, verbose_name='تایید شده')
    is_read = models.BooleanField(default=False, verbose_name='خوانده شده')

    def __str__(self):
        return self.title

    def get_abslute_url(self):
        return reverse('article-details', kwargs={'slug':self.slug})

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        return super().save(*args, **kwargs)