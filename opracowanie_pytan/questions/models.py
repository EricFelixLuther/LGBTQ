'''
Created on May 11, 2016

@author: k.maciejczuk
'''
from django.db import models


class Quiz_Set(models.Model):
    name = models.CharField(max_length=64, null=False, blank=False)

    @property
    def get_questions(self):
        return Question.objects.filter(quiz_set=self)

    def __unicode__(self):
        return self.name


class Question(models.Model):
    ANSWER_TYPES = (("Plain text", "Plain text"), ("List", "List"), ("Steps", "Steps"), ("Table", "Table"))
    question = models.CharField(max_length=256)
    hint = models.CharField(max_length=128, blank=True)
    answer = models.TextField()
    quiz_set = models.ForeignKey(Quiz_Set)
    answer_type=models.CharField(max_length=12, choices=ANSWER_TYPES)

    def __unicode__(self):
        return self.question
