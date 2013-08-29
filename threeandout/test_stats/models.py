from django.db import models
import datetime

POSITIONS = (
    ('QB', 'Quarterback'),
    ('WR', 'Wide Receiver'),
    ('RB', 'Running Back'),
    ('TE', 'Tight End'),
)

class NFLPlayer(models.Model):
    name = models.CharField(max_length=200)
    team = models.CharField(max_length=200)
    position = models.CharField(max_length=2, choices=POSITIONS)

class NFLWeeklyStat(models.Model):
    week              = models.IntegerField()
    score             = models.FloatField()
    recTd             = models.IntegerField() 
    fumbles           = models.IntegerField()
    interceptions     = models.IntegerField() 
    passTd            = models.IntegerField()
    passYds           = models.IntegerField()
    fumbleRecoveryTDs = models.IntegerField()
    rushYds           = models.IntegerField()
    recYds            = models.IntegerField()
    rushTd            = models.IntegerField()
    player            = models.ForeignKey(NFLPlayer)

class Picks(models.Model):
    week = models.IntegerField()
    qb = models.ForeignKey(NFLPlayer, related_name='qbpicks')
    rb = models.ForeignKey(NFLPlayer, related_name='rbpicks')
    te = models.ForeignKey(NFLPlayer, related_name='tepicks')
    wr = models.ForeignKey(NFLPlayer, related_name='wrpicks')
    score = models.FloatField()
    mod_time = models.DateTimeField(datetime.datetime.now)

class FFLPlayer(models.Model):
    name = models.CharField(max_length=200)
    email = models.CharField(max_length=100)
    league = models.IntegerField()
    picks = models.ManyToManyField(Picks)
    
    def calculateyearlyscore(self):
        #TODO: Calcuate the total score of all picks up to this point
        return 0
    
    scoretodate = property(calculateyearlyscore)
    
    
    

class NFLSchedule(models.Model):
    home = models.CharField(max_length=200)
    away = models.CharField(max_length=200)
    week = models.IntegerField()
    kickoff = models.DateTimeField(datetime.datetime.now)

