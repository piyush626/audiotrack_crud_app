from django import forms
from django.forms import fields
from django.forms.models import ModelForm
from .models import SongFile,PodcastFile,AudioBookFile,Participants

class SongForm(forms.ModelForm):
    
    class Meta:
        model = SongFile
        fields = '__all__'

class PodcastForm(forms.ModelForm):
    
    class Meta:
        model = PodcastFile
        fields = '__all__'

class AudioBookForm(forms.ModelForm):

    class Meta:
        model = AudioBookFile
        fields = '__all__'

class ParticipantForm(forms.ModelForm):

    class Meta:
        model = Participants
        fields = '__all__'

# class PodcastParticipantForm(MultiModelForm):
#     form_classes = {
#         'podcast': PodcastForm,
#         'participant': ParticipantForm,
#     }