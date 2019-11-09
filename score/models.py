from django.db import models
from players.models import Players
from django.utils import timezone


# players = Players.objects.all

# Create your models here.
class Score(models.Model):
    _id = models.ForeignKey(Players,on_delete=models.CASCADE,null=False)
    achievement = models.CharField(null=False,max_length=50)
    date = models.DateTimeField(default=timezone.datetime.now())
    percentage = models.IntegerField()
    level = models.IntegerField(null=False)
    expair = models.DateTimeField(null=True,blank=True)



    def __str__(self):
        return self.achievement