from django.db import models
from django.utils.text import slugify
from django.contrib.auth import get_user_model


class Articles(models.Model):

    thumbnail = models.ImageField(upload_to='articles/thumbnails')
    slug = models.SlugField(max_length=255, blank=True, null=True)
    title = models.CharField(max_length=255, null=False, blank=False)
    description = models.TextField()
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    publish_date = models.DateField(auto_now_add=True)
    last_updated = models.DateField(auto_now=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Articles, self).save(*args, **kwargs)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'Articles'
