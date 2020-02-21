from django.db import models


class Characters(models.Model):
    name = models.TextField()


class Comics(models.Model):
    title = models.TextField()
    date = models.TextField()
    chapter = models.TextField()
    image = models.TextField()
    characters = models.ManyToManyField(Characters)


