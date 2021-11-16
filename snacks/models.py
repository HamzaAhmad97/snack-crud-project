from django.db import models
from django.contrib.auth import get_user_model
from django.db.models.deletion import CASCADE

class Snack(models.Model):
    title = models.CharField(max_length=64)
    purchaser = models.ForeignKey(get_user_model(), on_delete=CASCADE)
    description = models.TextField()