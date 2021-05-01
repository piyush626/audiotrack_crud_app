# from django.core.exceptions import MultipleObjectsReturned
from django.db import models
# from django.contrib.auth.models import User
from django.db.models.deletion import CASCADE
from django.core.validators import MaxValueValidator 
# Create your models here.

# class CustomUser(models.Model):
#     user = models.ForeignKey(User,on_delete=CASCADE)


class SongFile(models.Model):
    id = models.IntegerField(primary_key=True,null=False,blank=False,unique=True)
    song_name = models.CharField(max_length=100,null=False,blank=False)
    duration_seconds = models.IntegerField(null=False,blank=False)
    upload_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.song_name



class PodcastFile(models.Model):
    id = models.IntegerField(primary_key=True,null=False,blank=False,unique=True)
    podcast_name = models.CharField(max_length=100,null=False,blank=False)
    duration_seconds = models.IntegerField(null=False,blank=False)
    upload_time = models.DateTimeField(auto_now_add=True)
    host = models.CharField(max_length=100,null=False,blank=False)
    Number_of_participant = models.PositiveIntegerField(default=0,validators=[MaxValueValidator(10)])

    def __str__(self):
        return self.podcast_name

    @property
    def candidates(self):
        return self.participants_set.all()


class Participants(models.Model):
    podcastfile = models.ForeignKey(PodcastFile,on_delete=models.CASCADE,null=True)
    participant_name = models.CharField(max_length=100,blank=True,null=True)

    def __str__(self):
        return self.participant_name



class AudioBookFile(models.Model):
    id = models.IntegerField(primary_key=True,null=False,blank=False,unique=True)
    title = models.CharField(max_length=100,null=False,blank=False)
    author = models.CharField(max_length=100,null=False,blank=False)
    narrator = models.CharField(max_length=100,null=False,blank=False)
    duration_seconds = models.IntegerField(null=False,blank=False)
    upload_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

