from django.db import models

# must import models for python to know this is a model class
class Show(models.Model):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=1000)
    rating = models.FloatField()
    network = models.CharField(max_length=200)
    episodes = models.IntegerField(default=0)
    cast = models.JSONField(default=[])
    
    def __str__(self):
        return self.name 

