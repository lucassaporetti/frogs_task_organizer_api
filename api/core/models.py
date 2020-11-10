from django.db import models
import uuid


class Task(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    status = models.CharField(max_length=50)
    name = models.CharField(max_length=500)
    date = models.CharField(max_length=50)
    time = models.CharField(max_length=50)
    task_type = models.CharField(max_length=50)
    priority = models.CharField(max_length=50)

    def __str__(self):
        return self.name
