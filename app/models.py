
from django.db import models
from user.models import User


# Create your models here.
class GlucoseLevel(models.Model):
    timestamp = models.DateTimeField()
    glucose_value = models.IntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.glucose_value)