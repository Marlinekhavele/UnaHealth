import uuid
from django.db import models


# Create your models here.
class GlucoseLevel(models.Model):
    id =  models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    Gerät = models.CharField(max_length=50)
    Seriennummer = models.UUIDField()
    Aufzeichnungstyp = models.IntegerField()
    Gerätezeitstempel = models.DateTimeField()
    user_id = models.UUIDField(default=uuid.uuid4, editable=False)
    Glukosewert_Verlauf = models.IntegerField()

    def __str__(self):
        return str(self.Gerät)