from django.db import models

# Create your models here.
class Art(models.Model):
    imgbase64 = models.TextField()
