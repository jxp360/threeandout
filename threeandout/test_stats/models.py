from django.db import models
import mongoengine

# Create your models here.
#class FFLWeeklyStats(model.Model):
#    qb_name = models.CharField(max_length=100)
#    rb_name = models.CharField(max_length=100)
#    wr_name = models.CharField(max_length=100)
#    te_name = models.CharField(max_length=100)
#    score = models.FloatField(default=0)

#class Player(models.Model):
class ffl_players_test(mongoengine.Document):
    name = mongoengine.StringField(max_length=200)
    email = mongoengine.StringField(max_length=100)
    #mod_time = models.DateTimeField('date stored')
    league = mongoengine.IntField()
    picks = mongoengine.ListField()
    #stats = models.ForeignKey(FFLWeeklyStats)
