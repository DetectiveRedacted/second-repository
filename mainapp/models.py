from django.db import models
import random
from datetime import datetime, timedelta

class UserLogin(models.Model):
    login = models.CharField(max_length=50)
    email = models.EmailField()
    time = models.DateTimeField()

    def __str__(self):
        return self.login