from django import forms
from .models import Game, Questions, Team
from django.forms import ModelForm


class GameForm(ModelForm):
    
    class Meta:
        model = Game
        fields = ['game_name']


class QuestionForm(ModelForm):
    
    class Meta:
        model = Questions
        fields = ['question_set',
        'question1',
        'question2',
        'question3',
        'question4',
        'question5',
        'question6',
        'question7',
        'question8',
        'question9',
        'question10',
        'question11',
        'question12', 
        ]

class AnswerForm(ModelForm):
    
    class Meta:
        model = Team
        fields = ['team_name',
        'question1', 'answer1',
        'question2', 'answer2',
        'question3', 'answer3',
        'question4', 'answer4',
        'question5', 'answer5',
        'question6', 'answer6',
        'question7', 'answer7',
        'question8', 'answer8',
        'question9', 'answer9',
        'question10', 'answer10',
        'question11', 'answer11',
        'question12', 'answer12',
        ]