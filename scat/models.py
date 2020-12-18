from django.db import models

# Create your models here.

class Game(models.Model):
    game_name = models.CharField(max_length=100)

    class Meta:
        ordering = ('game_name',)
        verbose_name = 'game'
        verbose_name_plural = 'game'
    
    def __str__(self):
        return self.game_name


class Questions(models.Model):
    question_set = models.IntegerField(default=0)
    question1 = models.CharField(max_length=500)
    question2 = models.CharField(max_length=500)
    question3 = models.CharField(max_length=500)
    question4 = models.CharField(max_length=500)
    question5 = models.CharField(max_length=500)
    question6 = models.CharField(max_length=500)
    question7 = models.CharField(max_length=500)
    question8 = models.CharField(max_length=500)
    question9 = models.CharField(max_length=500)
    question10 = models.CharField(max_length=500)
    question11 = models.CharField(max_length=500)
    question12 = models.CharField(max_length=500)
    game = models.ForeignKey(Game, on_delete=models.CASCADE, null=True)

    class Meta:
        verbose_name = 'question'
        verbose_name_plural = 'questions'

    
    


class Team(models.Model):
    team_name = models.CharField(max_length=200, blank=True)
    question1 = models.CharField(max_length=500, blank=True, null=True)
    answer1 = models.CharField(max_length=500, blank=True)
    question2 = models.CharField(max_length=500, blank=True, null=True)
    answer2 = models.CharField(max_length=500, blank=True)
    question3 = models.CharField(max_length=500, blank=True, null=True)
    answer3 = models.CharField(max_length=500, blank=True)
    question4 = models.CharField(max_length=500, blank=True, null=True)
    answer4 = models.CharField(max_length=500, blank=True)
    question5 = models.CharField(max_length=500, blank=True, null=True)
    answer5 = models.CharField(max_length=500, blank=True)
    question6 = models.CharField(max_length=500, blank=True, null=True)
    answer6 = models.CharField(max_length=500, blank=True)
    question7 = models.CharField(max_length=500, blank=True, null=True)
    answer7 = models.CharField(max_length=500, blank=True)
    question8 = models.CharField(max_length=500, blank=True, null=True)
    answer8 = models.CharField(max_length=500, blank=True)
    question9 = models.CharField(max_length=500, blank=True, null=True)
    answer9 = models.CharField(max_length=500, blank=True)
    question10 = models.CharField(max_length=500, blank=True, null=True)
    answer10 = models.CharField(max_length=500, blank=True)
    question11 = models.CharField(max_length=500, blank=True, null=True)
    answer11 = models.CharField(max_length=500, blank=True)
    question12 = models.CharField(max_length=500, blank=True, null=True)
    answer12 = models.CharField(max_length=500, blank=True)
    set = models.ForeignKey(Questions, on_delete=models.CASCADE, null=True)


    class Meta:
        verbose_name = 'answer'
        verbose_name_plural = 'answers'

    def __str__(self):
        return self.team_name