from django.db import models


# Create your models here.
class Credentials(models.Model):
    user_id=models.CharField(unique=True,max_length=400)
    username = models.CharField(max_length=200)
    password = models.CharField(max_length=200)

    def __str__(self):
        return self.username
