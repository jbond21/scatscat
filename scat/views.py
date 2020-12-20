from django.shortcuts import render, redirect, get_object_or_404
from .models import Game, Questions, Team
from .forms import GameForm, QuestionForm, AnswerForm
from django.db import IntegrityError
from django.core.exceptions import ObjectDoesNotExist



def home(request):

    return render(request, 'home.html')


def create_game(request):
    all_names = Game.objects.all()
    name = request.POST.get('game_name')
    print(name)
    print(all_names)
    form = GameForm(request.POST, request.FILES)
    if request.method == "POST":
        #print(request.POST)
        form = GameForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('gamelist') 

    return render(request, 'game.html', {'form':form})

def game_list(request):
    games = Game.objects.all()

    return render(request, 'game_list.html', {'games':games})

def create_questions(request, game, id):
    questions = Game.objects.filter(game_name=game)

    form = QuestionForm(request.POST, request.FILES)
    if request.method == "POST":
        #print(request.POST)
        form = QuestionForm(request.POST, request.FILES)
        if form.is_valid():
            question = form.save()
            question.game = Game.objects.filter(id__exact=id).get()
            question.save()
           
            return redirect('questionlist', game, id) 
    return render(request, 'questions.html', {'form':form, 'questions':questions})

def question_list(request, game, id):
    questions = Questions.objects.filter(game_id=id)

    return render(request, 'question_list.html', {'questions':questions})

def answer_questions(request, game, set, id):
    questions = Questions.objects.filter(question_set=set)
    question_id = Game.objects.get(game_name=game)
    print(question_id.id)

    form = AnswerForm(request.POST, request.FILES)
    if request.method == "POST":
        #print(request.POST)
        form = AnswerForm(request.POST, request.FILES)
        if form.is_valid():
            answer = form.save()
            answer.set = Questions.objects.filter(id__exact=id).get()
            answer.save()
           
            return redirect('questionlist', game, question_id.id) 

    return render(request, 'answers.html', {'form':form, 'questions':questions})

def answer_list(request, game, set, id):
    answers = Team.objects.filter(set_id=id)
    question = Game.objects.get(game_name=game)


    return render(request, 'answer_list.html', {'answers': answers, 'question':question})