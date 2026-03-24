from django.shortcuts import render
from .models import UserLogin
import random
from datetime import datetime, timedelta

def index(request):

    if UserLogin.objects.count() == 0:
        for _ in range(10):
            UserLogin.objects.create(
                login='user{}'.format(random.randint(1, 100)),
                email='horizon@gmail.com',
                time=datetime.now() - timedelta(hours=random.randint(0, 24))
            )

    users = UserLogin.objects.all()
    return render(request, 'index.html', {'users': users})