from django.http import HttpResponse
from django.shortcuts import render,get_object_or_404,HttpResponseRedirect
from .models import Participants, SongFile,PodcastFile,AudioBookFile
from .forms import SongForm,PodcastForm,AudioBookForm,ParticipantForm
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic import View
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin

class CustomLogin(LoginView):
    template_name = 'audio/login.html'
    fields = '__all__'
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('home')

def index(request):
    return render(request, 'audio/home.html')


class SongItemBucket(LoginRequiredMixin, ListView):
    model = SongFile
    context_object_name = 'songs'
    template_name = 'audio/list_song.html'

    


class SongItemDetail(LoginRequiredMixin, DetailView):
    model = SongFile
    context_object_name = 'details'
    template_name = 'audio/detail_song.html'


class SongItemCreate(LoginRequiredMixin, CreateView):
    model = SongFile
    template_name = 'audio/create_song.html'
    form_class = SongForm
    success_url = reverse_lazy('song-list')

class SongItemUpdate(LoginRequiredMixin, UpdateView):
    model = SongFile
    template_name = 'audio/create_song.html'
    form_class = SongForm
    success_url = reverse_lazy('song-list')

class SongItemDelete(LoginRequiredMixin, DeleteView):
    model = SongFile
    template_name = 'audio/delete_song.html'
    context_object_name = 'delItem'
    success_url = reverse_lazy('song-list')


class PodcastItemBucket(LoginRequiredMixin, ListView):
    model = PodcastFile
    context_object_name = 'podcasts'
    template_name = 'audio/list_podcast.html'

class PodcastItemDetail(LoginRequiredMixin, DeleteView):
    model = PodcastFile
    context_object_name = 'Poddetails'
    template_name = 'audio/detail_podcast.html'

# class PodcastView(View):
    
#     @method_decorator(login_required)
#     def get(self,request,pk=None):
#         if pk:
#             podcast = get_object_or_404(PodcastFile,pk=pk)
#             pod_form = PodcastForm(instance=podcast)
#             persons = podcast.candidates
#             participant_form = [ParticipantForm(prefix=str(person.id),instance=Participants()) for person in persons]
#             template = 'audio/create_podcast.html'
#         else:
#             pod_form = PodcastForm(instance=PodcastFile())
#             participant_form = [ParticipantForm(prefix=str(x),instance=Participants()) for x in range(10)]
#             template = 'audio/create_podcast.html'
#         context = {'podform':pod_form,'personform':participant_form}
#         return render(request,template,context)

#     @method_decorator(login_required)
#     def post(self,request):
#         context={}
#         pod_form = PodcastForm(request.POST,instance=PodcastFile())
#         participant_form = [ParticipantForm(request.POST,prefix=str(x),instance=Participants()) for x in range(10)]
#         if pod_form.is_valid() and all([pf.is_valid() for pf in participant_form]):
#             pod_form.save()
#             for pf in participant_form:
#                 pf.save()
#         context = {'podform':pod_form,'personform':participant_form}
#         template = 'audio/list_podcast.html'
#         return render(request,template,context)

    
class PodcastItemCreate(LoginRequiredMixin, CreateView):
    model = PodcastFile
    template_name = 'audio/create_podcast.html'
    form_class = PodcastForm
    success_url = reverse_lazy('participant-item-create')


class PodcastItemUpdate(LoginRequiredMixin, UpdateView):
    model = PodcastFile
    template_name = 'audio/create_podcast.html'
    form_class = PodcastForm
    success_url = reverse_lazy('participant-item-create')

class PodcastItemDelete(LoginRequiredMixin, DeleteView):
    model = PodcastFile
    template_name = 'audio/delete_podcast.html'
    context_object_name = 'delPodItem'
    success_url = reverse_lazy('podcast-list')


class ParticipantCreate(LoginRequiredMixin, CreateView):
    model = Participants
    template_name = 'audio/create_participant.html'
    form_class = ParticipantForm
    success_url = reverse_lazy('participant-item-create')


class AudiobookItemBucket(LoginRequiredMixin, ListView):
    model = AudioBookFile
    context_object_name = 'audiobooks'
    template_name = 'audio/list_audiobook.html'

class AudiobookItemDetail(LoginRequiredMixin, DetailView):
    model = AudioBookFile
    context_object_name = 'bookdetails'
    template_name = 'audio/detail_audiobook.html'

class AudiobookItemCreate(LoginRequiredMixin, CreateView):
    model = AudioBookFile
    template_name = 'audio/create_audiobook.html'
    form_class = AudioBookForm
    success_url = reverse_lazy('audiobook-list')

class AudiobookItemUpdate(LoginRequiredMixin, UpdateView):
    model = AudioBookFile
    template_name = 'audio/create_audiobook.html'
    form_class = AudioBookForm
    success_url = reverse_lazy('audiobook-list')

class AudiobookItemDelete(LoginRequiredMixin, DeleteView):
    model = AudioBookFile
    template_name = 'audio/delete_audiobook.html'
    context_object_name = 'delbookItem'
    success_url = reverse_lazy('audiobook-list')