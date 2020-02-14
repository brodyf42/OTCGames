from django.core.urlresolvers import reverse
from django.db import models
from datetime import date, timedelta


class Game(models.Model):
	title = models.CharField(max_length=256, unique=True)
	in_library = models.BooleanField(default=True,verbose_name='In Demo Library')

	def get_absolute_url(self):
		return reverse('GameTracker:game_detail',kwargs={'pk':self.pk})

	def get_played_games(self):
		return PlayedGame.objects.filter(game=self)

	def get_events(self):
		return [item.event for item in self.get_played_games()]

	def get_last_played(self):
		return max([event.date for event in self.get_events()])

	def get_month_plays(self):
		last_month = date.today() - timedelta(days=30)
		return self.get_played_games().filter(event__date__gte=last_month).count()

	def get_year_plays(self):
		last_year = date.today() - timedelta(days=365)
		return self.get_played_games().filter(event__date__gte=last_year).count()

	def get_play_delta(self):
		if len(self.get_events()) > 1:
			dates = [event.date for event in self.get_events()]
			dates.sort()
			deltas = [td.days for td in  [dates[i + 1] - dates[i] for i in range(len(dates)-1)]]
			return round(sum(deltas)/len(deltas))
		else:
			return 0

	def get_year_chart_data(self):
		labels = [year for year in range(2012,date.today().year+1)]
		values = []

		event_years = [event.date.year for event in self.get_events()]

		for year in labels:
			values.append(event_years.count(year))

		return {'labels':labels,'values':values}

	def get_month_chart_data(self):
		labels = []
		for year in range(2012,date.today().year+1):
			for m in ['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec']:
				labels.append(str(m + " " + str(year)))

		all_months = []
		for year in range(2012,date.today().year+1):
			for i in range(1,13):
				all_months.append((year,i))

		event_months = [(event.date.year,event.date.month) for event in self.get_events()]

		values = []
		for month in all_months:
			values.append(event_months.count(month))

		return {'labels':labels,'values':values}

	def __str__(self):
		return self.title

	class Meta:
		ordering = ['title']


class Event(models.Model):
	date = models.DateField(unique=True)
	player_count = models.PositiveSmallIntegerField(verbose_name='Number of Participants')
	games = models.ManyToManyField(Game, through='PlayedGame')

	def get_absolute_url(self):
		return reverse('GameTracker:event_detail',kwargs={'pk':self.pk})

	def get_played_games(self):
		return PlayedGame.objects.filter(event=self)

	def get_game_count(self):
		return games.count()

	def __str__(self):
		return self.date.strftime('%Y-%m-%d')

	class Meta:
		ordering = ['-date']


class PlayedGame(models.Model):
	event = models.ForeignKey(Event, on_delete=models.CASCADE)
	game = models.ForeignKey(Game, on_delete=models.CASCADE)
	game_player_count = models.PositiveSmallIntegerField()

	def __str__(self):
		return str(self.event) + " | " + str(self.game)

	class Meta:
		unique_together = ('event','game')
		ordering = ['event','game']
