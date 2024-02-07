from django.db import models

# Create your models here.

class Player(models.Model):
    name = models.CharField(max_length=100)
    money = models.IntegerField(default=0)
    color_code = models.CharField(max_length=20, default="#000000")

    def __str__(self):
        return self.name