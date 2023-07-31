from django.db import models

class Movie(models.Model):
    title = models.CharField(max_length=63)
    description = models.CharField(max_length=255, blank=True, null=True)
    duration = models.IntegerField()

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "movies"


