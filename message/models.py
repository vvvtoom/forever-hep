from django.db import models

# Create your models here.

class Message(models.Model):
    id = models.AutoField(primary_key=True)
    message_writer = models.CharField(max_length=20)
    message_content = models.CharField(max_length=400)

    def __str__(self):
        return self.message_writer