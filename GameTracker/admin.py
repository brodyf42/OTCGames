from django.contrib import admin
from GameTracker.models import Game,Event,PlayedGame

# Register your models here.
admin.site.register(Game)
admin.site.register(Event)
admin.site.register(PlayedGame)
