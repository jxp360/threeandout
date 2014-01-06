from django.db import models
import datetime
from django.contrib.auth.models import User
from django.db.models import Q

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
    
    def __unicode__(self):
        return self.name
    

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


class FFLPlayer(models.Model):
    user = models.ForeignKey(User)
    #name = models.CharField(max_length=200)
    teamname = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    league = models.IntegerField(default=0)
    
    def calculateyearlyscore(self):
        #TODO: Calcuate the total score of all picks up to this point
        totalPicks = Picks.objects.filter(fflPlayer=self)
        return sum([x.score for x in totalPicks])

    scoretodate = property(calculateyearlyscore)
    
    def __unicode__(self):
        return self.teamname

class Picks(models.Model):
    week = models.IntegerField()
    qb = models.ForeignKey(NFLPlayer, related_name='qbpicks')
    rb = models.ForeignKey(NFLPlayer, related_name='rbpicks')
    te = models.ForeignKey(NFLPlayer, related_name='tepicks')
    wr = models.ForeignKey(NFLPlayer, related_name='wrpicks')
    #score = models.FloatField()
    fflPlayer = models.ForeignKey(FFLPlayer, related_name='fflPlayer')
    mod_time = models.DateTimeField(datetime.datetime.now)
    def calculatescore(self):
        #query the NFLWeeklyStats for the players for this week
        #query for each of my players and the right week
        query = (Q(player=self.qb) | Q(player=self.rb) | Q(player=self.wr) | Q(player=self.te)) & Q(week=self.week)
        stats = NFLWeeklyStat.objects.filter(query)
        if not len(stats) in (0,4):
          print "ERROR - we don't have enough stats!"
          print stats
          #raise RuntimeError("wrong number of stats retrieved")
        return sum([x.score for x in stats])
    score = property(calculatescore)

class NFLSchedule(models.Model):
    home = models.CharField(max_length=200)
    away = models.CharField(max_length=200)
    week = models.IntegerField()
    kickoff = models.DateTimeField(datetime.datetime.now)


class Standing(models.Model):
    fflPlayer = models.ForeignKey(FFLPlayer, related_name='standingPlayer')
    scoretodate = models.FloatField()
    week1 = models.FloatField()
    week2 = models.FloatField()
    week3 = models.FloatField()
    week4 = models.FloatField()
    week5 = models.FloatField()
    week6 = models.FloatField()
    week7 = models.FloatField()
    week8 = models.FloatField()
    week9 = models.FloatField()
    week10 = models.FloatField()
    week11 = models.FloatField()
    week12 = models.FloatField()
    week13 = models.FloatField()
    week14 = models.FloatField()
    week15 = models.FloatField()
    week16 = models.FloatField()
    week17 = models.FloatField()
    
    def __unicode__(self):
        return self.fflPlayer.teamname


class madePlayoffs(models.Model):
    fflPlayer = models.ForeignKey(FFLPlayer)   
    
    def __unicode__(self):
        return self.fflPlayer.teamname 

class PlayoffStanding(models.Model):
    fflPlayer = models.ForeignKey(FFLPlayer, related_name='playoffStandingPlayer')
    scoretodate = models.FloatField()
    week1 = models.FloatField()
    week2 = models.FloatField()
    week3 = models.FloatField()

    def __unicode__(self):
        return self.fflPlayer.teamname

