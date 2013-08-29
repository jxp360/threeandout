from django.db import models
import datetime
from django.contrib.auth.models import User

POSITIONS = (
    ('QB', 'Quarterback'),
    ('WR', 'Wide Receiver'),
    ('RB', 'Running Back'),
    ('TE', 'Tight End'),
)

class NFLWeeklyStat(models.Model):
    week =  models.IntegerField()
    score =  models.FloatField()

class NFLPlayer(models.Model):
    name = models.CharField(max_length=200)
    team = models.CharField(max_length=200)
    position = models.CharField(max_length=2, choices=POSITIONS)
    stats = models.ManyToManyField(NFLWeeklyStat)

class Picks(models.Model):
    week = models.IntegerField()
    qb = models.ForeignKey(NFLPlayer, related_name='qbpicks')
    rb = models.ForeignKey(NFLPlayer, related_name='rbpicks')
    te = models.ForeignKey(NFLPlayer, related_name='tepicks')
    wr = models.ForeignKey(NFLPlayer, related_name='wrpicks')
    score = models.FloatField()
    mod_time = models.DateTimeField(datetime.datetime.now)

class FFLPlayer(models.Model):
    user = models.ForeignKey(User)
    #name = models.CharField(max_length=200)
    email = models.CharField(max_length=100)
    league = models.IntegerField()
    picks = models.ManyToManyField(Picks)
    
    def calculateyearlyscore(self):
        #TODO: Calcuate the total score of all picks up to this point
        return 0
    
    scoretodate = property(calculateyearlyscore)
    
    
    

