from django.db import models
from players.models import Players
from django.utils import timezone


# players = Players.objects.all

# Create your models here.
class Score(models.Model):
    _id = models.ForeignKey(Players,on_delete=models.CASCADE,null=False)
    date = models.DateTimeField(default=timezone.datetime.now())
    expair = models.DateTimeField(null=True,blank=True)
    shield_spell_u = models.IntegerField(null=True)
    slo_mo_spell_u = models.IntegerField(null=True)
    productive_spell_u = models.IntegerField(null=True)
    momentum_spell_u = models.IntegerField(null=True)
    healing_spell_u = models.IntegerField(null=True)
    one_scene_u = models.IntegerField(null=True)
    two_scene_u = models.IntegerField(null=True)
    three_scene_u = models.IntegerField(null=True)
    four_scene_u = models.IntegerField(null=True)
    five_scene_u = models.IntegerField(null=True)
    six_scene_u = models.IntegerField(null=True)
    seven_scene_u = models.IntegerField(null=True)
    eight_scene_u = models.IntegerField(null=True)
    nine_scene_u = models.IntegerField(null=True)
    ten_scene_u = models.IntegerField(null=True)
    one_fruits_u = models.IntegerField(null=True)
    two_fruits_u = models.IntegerField(null=True)
    three_fruits_u = models.IntegerField(null=True)
    four_fruits_u = models.IntegerField(null=True)
    five_fruits_u = models.IntegerField(null=True)
    six_fruits_u = models.IntegerField(null=True)
    seven_fruits_u = models.IntegerField(null=True)
    eight_fruits_u = models.IntegerField(null=True)
    nine_fruits_u = models.IntegerField(null=True)
    ten_fruits_u = models.IntegerField(null=True)
    eleven_fruits_u = models.IntegerField(null=True)
    twelve_fruits_u = models.IntegerField(null=True)
    thirteen_fruits_u = models.IntegerField(null=True)
    fourteen_fruits_u = models.IntegerField(null=True)
    fifteen_fruits_u = models.IntegerField(null=True)
    sixteen_fruits_u = models.IntegerField(null=True)
    seventeen_fruits_u = models.IntegerField(null=True)
    eighteen_fruits_u = models.IntegerField(null=True)
    nineteen_fruits_u = models.IntegerField(null=True)
    twenty_fruits_u = models.IntegerField(null=True)
    twentyone_fruits_u = models.IntegerField(null=True)
    twentytwo_fruits_u = models.IntegerField(null=True)
    twentythree_fruits_u = models.IntegerField(null=True)
    twentyfour_fruits_u = models.IntegerField(null=True)
    twentyfive_fruits_u = models.IntegerField(null=True)
    dead = models.IntegerField(null=True)
    total_fruits = models.IntegerField(null=True)
    fblogin = models.CharField(default='deactive',max_length=10)
    



    def __str__(self):
        return self.fblogin