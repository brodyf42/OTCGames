from django.conf.urls import url
from GameTracker import views

app_name = 'GameTracker'

urlpatterns = [
	url(r'^$',views.event_list_view,name='index'),
	# Event patterns
	url(r'^events/$',views.event_list_view,name='event_list'),
	url(r'^events/new/$',views.EventCreateView.as_view(),name='event_new'),
	url(r'^events/delete/(?P<pk>\d+)/$',views.EventDeleteView.as_view(),name='event_delete'),
	url(r'^events/update/(?P<pk>\d+)/$',views.EventUpdateView.as_view(),name='event_update'),
	url(r'^events/(?P<pk>\d+)/$',views.EventDetailView.as_view(),name='event_detail'),
	# Game patterns
	url(r'^games/$',views.game_list_view,name='game_list'),
	url(r'^games/new/$',views.GameCreateView.as_view(),name='game_new'),
	url(r'^games/delete/(?P<pk>\d+)/$',views.GameDeleteView.as_view(),name='game_delete'),
	url(r'^games/update/(?P<pk>\d+)/$',views.GameUpdateView.as_view(),name='game_update'),
	url(r'^games/(?P<pk>\d+)/$',views.GameDetailView.as_view(),name='game_detail'),
	# PlayedGame patterns
	url(r'^playedgame/new/(?P<pk>\d+)/$',views.new_played_game_view,name='played_game_new'),
	url(r'^playedgame/delete/(?P<pk>\d+)/$',views.delete_played_game_view,name='played_game_delete'),
]
