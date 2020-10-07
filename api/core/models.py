from django.db import models


class Task(models.Model):
    id = models.AutoField(primary_key=True)
    status = models.CharField(max_length=50)
    name = models.CharField(max_length=500)
    date = models.CharField(max_length=50)
    time = models.CharField(max_length=50)
    type = models.CharField(max_length=50)
    priority = models.CharField(max_length=50)

    def __str__(self):
        return self.name
