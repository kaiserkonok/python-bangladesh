from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=180)

    def __str__(self):
        return self.title
