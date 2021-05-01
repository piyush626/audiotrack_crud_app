from django.contrib import admin

# Register your models here.
from .models import SongFile,PodcastFile,AudioBookFile,Participants

admin.site.register(SongFile)
admin.site.register(PodcastFile)
admin.site.register(AudioBookFile)
admin.site.register(Participants)