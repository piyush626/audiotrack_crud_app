from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('login/',views.CustomLogin.as_view(), name='login'),
    path('logout/',LogoutView.as_view(next_page='login'), name='logout'),
    path('',views.index,name='home'),
    path('song-list',views.SongItemBucket.as_view(), name='song-list'),
    path('song-item/<int:pk>/',views.SongItemDetail.as_view(), name='song-item'),
    path('song-item-create/',views.SongItemCreate.as_view(), name='song-item-create'),
    path('song-item-update/<int:pk>/',views.SongItemUpdate.as_view(), name='song-item-update'),
    path('song-item-delete/<int:pk>/',views.SongItemDelete.as_view(), name='song-item-delete'),

    #path('create/',views.create_view,name='create'),
    #path('retrieve/',views.list_view,name='retrieve'),
    #path('<id>/delete', views.delete_view,name='delete'),

    path('podcast-list',views.PodcastItemBucket.as_view(), name='podcast-list'),
    path('podcast-item/<int:pk>/',views.PodcastItemDetail.as_view(), name='podcast-item'),
    path('podcast-item-create/',views.PodcastItemCreate.as_view(), name='podcast-item-create'),
    path('podcast-item-update/<int:pk>/',views.PodcastItemUpdate.as_view(), name='podcast-item-update'),
    path('podcast-item-delete/<int:pk>/',views.PodcastItemDelete.as_view(), name='podcast-item-delete'),
    path('participant-item-create/',views.ParticipantCreate.as_view(), name='participant-item-create'),
   

    path('audiobook-list',views.AudiobookItemBucket.as_view(), name='audiobook-list'),
    path('audiobook-item/<int:pk>/',views.AudiobookItemDetail.as_view(), name='audiobook-item'),
    path('audiobook-item-create/',views.AudiobookItemCreate.as_view(), name='audiobook-item-create'),
    path('audiobook-item-update/<int:pk>/',views.AudiobookItemUpdate.as_view(), name='audiobook-item-update'),
    path('audiobook-item-delete/<int:pk>/',views.AudiobookItemDelete.as_view(), name='audiobook-item-delete'),

    #path('/audio/<int:pk>',)
]