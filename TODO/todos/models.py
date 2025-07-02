from django.db import models

class Todo(models.Model):
    id = models.AutoField(primary_key=True) 
    title = models.CharField(max_length=200)
    body = models.TextField(default="empty")

    def __str__(self):
        return self.title

# Create your models here.clear

