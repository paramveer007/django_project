from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.

'''
1. write your table class
2. python manage.py makemigrations
3. python manage.py sqlmigrate blog 0001 (<app_name> = blog, <migation_number> = 0001)
4. python manage.py migrate --> This will create the table in put data base
'''

class Posts(models.Model):
    title = models.CharField(max_length = 100)
    content = models.TextField()
    date_posted = models.DateTimeField(default = timezone.now)
    author = models.ForeignKey(User, on_delete = models.CASCADE)

    def __str__(self):
        return self.title