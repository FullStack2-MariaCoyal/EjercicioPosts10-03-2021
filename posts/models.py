from django.db import models

# Create your models here.

class Post(models.Model):
    mail = models.EmailField(default="")
    nombre = models.TextField(default="")
    def __str__(self):
        return self.mail