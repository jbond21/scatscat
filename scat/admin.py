from django.contrib import admin
from .models import Game, Questions, Team

# Register your models here.

class GameAdmin(admin.ModelAdmin):
    list_display = ['id', 'game_name']

admin.site.register(Game, GameAdmin)

class QuestionsAdmin(admin.ModelAdmin):
    list_display = ['id', 'game', 'question_set']

admin.site.register(Questions, QuestionsAdmin)
admin.site.register(Team)
