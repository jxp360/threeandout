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

class NFLTeam(models.Model):
    city = models.CharField(max_length=200)
    name = models.CharField(max_length=200)
    short_name = models.CharField(max_length=3)
    
    def __unicode__(self):
        return self.name

class NFLPlayer(models.Model):
    name = models.CharField(max_length=200)
    team = models.ForeignKey(NFLTeam)
    position = models.CharField(max_length=2, choices=POSITIONS)
    nfldb_id = models.CharField(max_length=10)
    def __unicode__(self):
        return self.name

class ScoringSystem(models.Model):
    function=models.CharField(max_length=100)

class NFLSchedule(models.Model):
    home = models.ForeignKey(NFLTeam, related_name='homeGames')
    away = models.ForeignKey(NFLTeam, related_name='awayGames')
    week = models.IntegerField()
    season_type =  models.CharField(max_length=10)
    kickoff = models.DateTimeField(datetime.datetime.now)
    nfldb_id = models.CharField(max_length=10)
    scoring_system = models.ForeignKey(ScoringSystem)
    def __unicode__(self):
        return self.away.short_name + " @ " + self.home.short_name

class NFLWeeklyStat(models.Model):
    score             = models.FloatField()
    defaultScore      = models.FloatField()
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
    game              = models.ForeignKey(NFLSchedule)    
    
    def __unicode__(self):
        return self.player.name + " " +self.player.team.short_name + " week:" + str(self.game.week)


class FFLPlayer(models.Model):
    user = models.ForeignKey(User)
    #name = models.CharField(max_length=200)
    teamname = models.CharField(max_length=100)
    displayName = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    league = models.IntegerField(default=0)
    autoPickPreference = models.BooleanField(default=True)
    
    def calculateyearlyscore(self):
        #TODO: Calcuate the total score of all picks up to this point
        #totalPicks = Picks.objects.filter(fflPlayer=self).filter(week__lte=17)
        totalPicks = Picks.objects.filter(fflplayer=self)
        return sum([x.score for x in totalPicks])

    scoretodate = property(calculateyearlyscore)
    
    def __unicode__(self):
        return self.teamname

class Picks(models.Model):
    week = models.IntegerField()
    season_type =  models.CharField(max_length=10)
    qb = models.ForeignKey(NFLPlayer, related_name='qbpicks')
    rb = models.ForeignKey(NFLPlayer, related_name='rbpicks')
    te = models.ForeignKey(NFLPlayer, related_name='tepicks')
    wr = models.ForeignKey(NFLPlayer, related_name='wrpicks')
    #score = models.FloatField()
    fflplayer = models.ForeignKey(FFLPlayer, related_name='fflPlayer')
    mod_time = models.DateTimeField(datetime.datetime.now)
    def calculatescore(self):
        #query the NFLWeeklyStats for the players for this week
        #query for each of my players and the right week
        query = (Q(player=self.qb) | Q(player=self.rb) | Q(player=self.wr) | Q(player=self.te)) & Q(game__week=self.week) & Q(game__season_type=self.season_type)
        stats = NFLWeeklyStat.objects.filter(query)
        if not len(stats) in (0,4):
          print "ERROR - we don't have enough stats!"
          print stats
          #raise RuntimeError("wrong number of stats retrieved")
        return sum([x.score for x in stats])
    score = property(calculatescore)

class Standing(models.Model):
    fflplayer = models.ForeignKey(FFLPlayer, related_name='standingPlayer')
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
        return self.fflplayer.teamname


class madePlayoffs(models.Model):
    fflplayer = models.ForeignKey(FFLPlayer)   
    
    def __unicode__(self):
        return self.fflplayer.teamname 

class PlayoffStanding(models.Model):
    fflplayer = models.ForeignKey(FFLPlayer, related_name='playoffStandingPlayer')
    scoretodate = models.FloatField()
    week1 = models.FloatField()
    week2 = models.FloatField()
    week3 = models.FloatField()

    def __unicode__(self):
        return self.fflplayer.teamname

