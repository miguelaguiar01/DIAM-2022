from django.db import models
from django.template.defaultfilters import slufigy
from django.contrib.auth.models import User
from django.urls import reverse

# Create models here: 

class cadeira(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    slug = models.SlugField(unique= True, max_length=255)
    
    def get_absolute_url(self):
        return reverse("cadeira_detail", args={self.slug})
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super(cadeira,self).save(*args, **kwargs)
    