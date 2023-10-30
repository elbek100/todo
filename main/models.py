from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class Service(models.Model):
    text1 = models.CharField(max_length=150),
    expires_at = models.DateTimeField(auto_now_add=True),
    owner_id = models.ForeignKey(User, models.CASCADE)




