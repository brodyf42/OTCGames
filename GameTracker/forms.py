from django import forms
from GameTracker.models import Event,Game,PlayedGame


class DateInput(forms.DateInput):
	input_type = 'date'


class EventForm(forms.ModelForm):

	class Meta():
		model = Event
		fields = ('date','player_count')

		widgets = {
			'date':DateInput(attrs={'class':'form-control'}),
			'player_count':forms.NumberInput(attrs={'class':'form-control'})
		}


class GameForm(forms.ModelForm):

	class Meta():
		model = Game
		fields = ('title','in_library')

		widgets = {
			'title':forms.TextInput(attrs={'class':'form-control'}),
			'in_library':forms.CheckboxInput()
		}


class NewPlayedGameForm(forms.ModelForm):

	class Meta():
		model = PlayedGame
		fields = ['game','game_player_count']

		widgets = {
			'game':forms.Select(attrs={'class':'form-control'}),
			'game_player_count':forms.NumberInput(attrs={'class':'form-control'})
		}
