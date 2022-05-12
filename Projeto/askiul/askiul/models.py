from django.db import models

class Cadeira(models.Model):
    name = models.CharField(max_length=200)
    descrição = models.CharField(max_length=200)
    def __str__(self):
        return self.name


class ListaCadeiras(models.Model):
    title = models.CharField(max_length=100, unique=True)

    def get_absolute_url(self):
        return reverse("list", args=[self.id])

    def __str__(self):
        return self.title