from django.db import models
import random
from datetime import datetime, timedelta

class UserLogin(models.Model):
    login = models.CharField(max_length=50)
    email = models.EmailField()
    time = models.DateTimeField()

    def save(self, *args, **kwargs):

        if not self.time:
            self.time = datetime.now() - timedelta(hours=random.randint(0, 24))
        super().save(*args, **kwargs)