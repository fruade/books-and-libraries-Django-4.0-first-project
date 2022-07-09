from django.db import models

class FeedBack(models.Model):
    name = models.CharField(max_length=16)
    surname = models.CharField(max_length=30)
    rating = models.PositiveIntegerField()
    feedback = models.TextField()
