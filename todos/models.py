from django.db import models
from django.contrib.auth.models import User
from django.utils import dateformat

# Create your models here.


class Todo(models.Model):

    def __str__(self):
        return self.title

    title = models.TextField(max_length=20)
    content = models.TextField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    status = models.BooleanField()
    updated_at = models.DateTimeField(auto_now=True)

    # def updated_at(self):
    #     # return dateformat.format(self.updated_at, 'Y/n/d H:i:s')
    #     return type(self.updated_at | date)
