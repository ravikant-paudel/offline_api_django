
from django.db import models

class UserProfile(models.Model):
    username = models.CharField(max_length=255)
    age = models.PositiveBigIntegerField()

    def __str__(self):
        return self.username 
