from django.db import models

# Create your models here.

class Buzon(models.Model):
    asunto=models.CharField(max_length=100)
    mensaje=models.CharField(max_length=800)