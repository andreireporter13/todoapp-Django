from django.db import models


class Tasks(models.Model):
    task = models.CharField(max_length=100)
    done_task = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.task} <---> {self.done_task}'
