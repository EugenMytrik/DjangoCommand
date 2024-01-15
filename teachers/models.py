from django.db import models


class Teacher(models.Model):
    job = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
