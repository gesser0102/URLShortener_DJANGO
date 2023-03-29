from django.db import models

class ShortURL(models.Model):
    original_url = models.URLField(max_length=700, verbose_name="")
    short_url = models.CharField(max_length=8, unique=True)

    def __str__(self):
        return self.original_url