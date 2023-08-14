from django.db import models
from django.contrib.auth import get_user_model
from datetime import date
from django.urls import reverse


class TodoList(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    task_date = models.DateField(default=date.today)
    task = models.TextField()
    task_is_done = models.BooleanField(default=False)

    def get_absolute_url(self):
        return reverse('tasks')

    def __str__(self):
        return f"{self.user.username}: {self.task}"
