from django.db import models
from django.utils import timezone

# Create your models here.
class Players(models.Model):
    _id = models.CharField(primary_key=True,null=False,max_length=15)
    date = models.DateTimeField(default=timezone.datetime.now())
    email = models.CharField(null=False,max_length=64)
    xp = models.IntegerField(null=False)
    coin = models.IntegerField(null=True)
    image = models.ImageField(null=True,upload_to='images/')
    name = models.CharField(null=True,max_length=64)
    playing = models.IntegerField(default=1)
    country = models.CharField(null=False,max_length=15)

    def __str__(self):
        return self._id
