import re
from django.core.urlresolvers import reverse_lazy
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render,redirect,get_object_or_404
from django.views.generic import View,TemplateView,ListView,DetailView,CreateView,DeleteView,UpdateView
from GameTracker.models import Game,Event,PlayedGame
from GameTracker.forms import EventForm,GameForm,NewPlayedGameForm


# Event views

class EventCreateView(CreateView):
	model = Event
	form_class = EventForm


class EventDeleteView(DeleteView):
	model = Event
	success_url = reverse_lazy('GameTracker:event_list')


class EventUpdateView(UpdateView):
	model = Event
	form_class = EventForm


class EventDetailView(DetailView):
	model = Event

	# Need in include form for adding played games to the event
	def get(self, request, *args, **kwargs):
		self.object = self.get_object()
		played_game_form = NewPlayedGameForm(self.request.GET or None)
		context = self.get_context_data(**kwargs)
		context['played_game_form'] = played_game_form
		return self.render_to_response(context)


def event_list_view(request):
	event_list = Event.objects.all()
	paginator = Paginator(event_list, 10)
	page = request.GET.get('page')

	try:
		events = paginator.page(page)
		page = int(page)
		if paginator.num_pages > 10:
			if page <= 6:
				nav_list = list(range(1,11))
			elif paginator.num_pages - page < 6:
				nav_list = list(range(paginator.num_pages-10,paginator.num_pages+1))
			else:
				nav_list = list(range(page-5,page+6))
		else:
			nav_list = list(range(1,paginator.num_pages+1))
	except PageNotAnInteger:
		# If page is not an integer, deliver first page.
		return redirect('/events/?page=1')
	except EmptyPage:
		# If page is out of range (e.g. 9999), deliver last page of results.
		return redirect('/events/?page=' + str(paginator.num_pages))

	return render(request, 'GameTracker/event_list.html', {'events': events,'nav_list':nav_list})


# Game Views

class GameCreateView(CreateView):
	model = Game
	form_class = GameForm


class GameDeleteView(DeleteView):
	model = Game
	success_url = reverse_lazy('GameTracker:game_list')


class GameUpdateView(UpdateView):
	model = Game
	form_class = GameForm


class GameDetailView(DetailView):
	model = Game


def game_list_view(request):
	category = request.GET.get('category')

	try:
		pattern = re.compile("^[a-zA-Z]$")
		if category == 'other':
			games = Game.objects.exclude(title__regex=r'^[a-zA-Z]')
		elif pattern.match(category):
			games = Game.objects.filter(title__istartswith=category)
		else:
			games = Game.objects.all()
			category = 'all'
	except:
		games = Game.objects.all()
		category = 'all'

	return render(request, 'GameTracker/game_list.html', {'games': games,'category':category})


# PlayedGame Views

def new_played_game_view(request,pk):
	event = get_object_or_404(Event,pk=pk)
	form = NewPlayedGameForm(request.POST)

	if form.is_valid():
		played_game = form.save(commit=False)
		played_game.event = event
		played_game.save()

	return redirect('/events/' + str(pk))


def delete_played_game_view(request,pk):
	pg_instance = get_object_or_404(PlayedGame,pk=pk)
	event_pk = pg_instance.event.pk
	pg_instance.delete()

	return redirect('/events/' + str(event_pk))
